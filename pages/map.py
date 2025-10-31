# pages/map.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Shanghai Lens", layout="wide")

API_KEY = st.secrets.get("GOOGLE_MAPS_API_KEY", "")
st.title("Map of Shanghai")
st.caption("Pan/zoom, click to drop a marker, search places. Selection persists in the browser.")

if not API_KEY:
    st.error("Missing GOOGLE_MAPS_API_KEY in .streamlit/secrets.toml")
    st.stop()

# NOTE: This is a NORMAL triple-quoted string (NOT an f-string), so JS { } are safe.
html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    html, body {
      margin: 0; padding: 0; height: 100%; width: 100%;
      font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    }
    .wrap {
      display: grid; grid-template-rows: auto 1fr auto; gap: 8px;
      height: 100%; padding: 8px; box-sizing: border-box;
    }
    .topbar { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
    #map { width: 100%; height: 520px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,.08); }
    input#search { flex: 1 1 360px; padding: 8px 10px; border: 1px solid #d0d7de; border-radius: 8px; outline: none; }
    .panel { font-size: 14px; padding: 8px 10px; border: 1px solid #e5e7eb; border-radius: 8px; background: #fafafa; }
    .btn { padding: 8px 12px; border: 1px solid #d0d7de; border-radius: 8px; background: white; cursor: pointer; }
    .btn:active { transform: translateY(1px); }
    code { background:#f6f8fa; padding:2px 6px; border-radius:6px; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="topbar">
      <input id="search" placeholder="Search a place (e.g., The Bund / Lujiazui / Pudong)" />
      <button id="clearBtn" class="btn">Clear selection</button>
      <button id="downloadBtn" class="btn">Download JSON</button>
    </div>

    <div id="map"></div>

    <div class="panel">
      <div><strong>Latitude:</strong> <code id="lat">—</code> &nbsp;&nbsp; <strong>Longitude:</strong> <code id="lng">—</code></div>
      <div style="margin-top:6px;"><strong>Address:</strong> <span id="addr">(none)</span></div>
    </div>
  </div>

  <script>
    let map, marker, geocoder, autocomplete;
    const STORAGE_KEY = "shlens_google_map_selected";

    function loadSaved() {
      try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null"); } catch { return null; }
    }
    function saveSelected(p) { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(p)); } catch {} }
    function clearSelected() { try { localStorage.removeItem(STORAGE_KEY); } catch {} }

    function setInfo(lat, lng, address) {
      document.getElementById('lat').textContent = (lat != null ? lat.toFixed(6) : "—");
      document.getElementById('lng').textContent = (lng != null ? lng.toFixed(6) : "—");
      document.getElementById('addr').textContent = address || "(none)";
    }

    function setMarker(position) {
      if (!marker) {
        marker = new google.maps.Marker({ position, map, draggable: true });
        marker.addListener("dragend", () => {
          const p = marker.getPosition();
          handlePosition(p);
        });
      } else {
        marker.setPosition(position);
      }
    }

    function handlePosition(latLng) {
      const lat = latLng.lat();
      const lng = latLng.lng();
      geocoder.geocode({ location: latLng }, (results, status) => {
        let address = null;
        if (status === "OK" && results && results[0]) {
          address = results[0].formatted_address;
        }
        setInfo(lat, lng, address);
        saveSelected({ lat, lng, address });
      });
    }

    function initMap() {
      const shanghai = { lat: 31.2304, lng: 121.4737 };
      map = new google.maps.Map(document.getElementById("map"), {
        center: shanghai, zoom: 11, mapTypeId: "roadmap", gestureHandling: "greedy"
      });

      geocoder = new google.maps.Geocoder();

      map.addListener("click", (e) => {
        setMarker(e.latLng);
        handlePosition(e.latLng);
      });

      const input = document.getElementById("search");
      const opts = { fields: ["geometry", "name", "formatted_address"], types: ["geocode"] };
      autocomplete = new google.maps.places.Autocomplete(input, opts);
      autocomplete.bindTo("bounds", map);
      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        if (!place || !place.geometry) return;
        const loc = place.geometry.location;
        map.panTo(loc);
        map.setZoom(14);
        setMarker(loc);
        const lat = loc.lat(), lng = loc.lng();
        const address = place.formatted_address || place.name || "";
        setInfo(lat, lng, address);
        saveSelected({ lat, lng, address });
      });

      const saved = loadSaved();
      if (saved && saved.lat && saved.lng) {
        const pos = new google.maps.LatLng(saved.lat, saved.lng);
        map.setCenter(pos);
        map.setZoom(13);
        setMarker(pos);
        setInfo(saved.lat, saved.lng, saved.address || "");
      }

      document.getElementById("clearBtn").addEventListener("click", () => {
        clearSelected();
        if (marker) marker.setMap(null);
        marker = null;
        setInfo(null, null, "");
      });

      document.getElementById("downloadBtn").addEventListener("click", () => {
        const raw = localStorage.getItem(STORAGE_KEY) || "{}";
        const blob = new Blob([raw], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url; a.download = "selected_location.json";
        document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
      });
    }
  </script>

  <!-- API key injected below -->
  <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=__API_KEY__&language=en&libraries=places&callback=initMap">
  </script>
</body>
</html>
"""

# inject your key safely
html = html.replace("__API_KEY__", API_KEY)

components.html(html, height=650, scrolling=False)

st.caption("Produce by GOOGLE MAP")
