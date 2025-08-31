# OpenNotification-HACS

<p align="right">
<img width="128" alt="Logo" src="https://raw.githubusercontent.com/HenriSaumure/OpenNotification-HACS/refs/heads/main/custom_components/opennotification/logo.png">
</p>

A custom Home Assistant component for sending push notification to clients via OpenNotification-API [official server](https://api.opennotification.org/) or a custom OpenNotification-API server

<br>

## Installation

### Method 1: HACS (Recommended)

1. Ensure HACS is installed and configured in your Home Assistant instance.
2. Add this repository as a **custom integration** under **HACS → Integrations → … (top-right) → Custom repositories**.

   * **Repository URL**: `https://github.com/HenriSaumure/OpenNotification-HACS`
   * **Category**: Integration
3. Search for **OpenNotification** in HACS and click **Install**.
4. Restart Home Assistant.

### Method 2: Manual installation

1. Clone this repository into your Home Assistant `custom_components` folder:

   ```yaml
   config/
   └── custom_components/
       └── opennotification/
           ├── __init__.py
           ├── manifest.json
           └── ...
   ```
2. Restart Home Assistant.

## Android Client

<table>
  <tr>
    <td>
      <p>
        <a href="https://github.com/HenriSaumure/OpenNotification-Client">
          OpenNotification Android Client
        </a>
      </p>
      <p>
        A lightweight Android app for receiving notifications from any OpenNotification-API server
      </p>
    </td>
    <td>
      <img width="256" alt="Logo" src="https://opennotification.org/images/Client.png">
    </td>
  </tr>
</table>
