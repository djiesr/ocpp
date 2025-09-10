## ⚠️ Important — Do NOT Update Your Grizzl-E Charger

> **Warning**  
> After the latest firmware update, your Grizzl-E charger will **no longer work** with your OCPP server in Home Assistant.  

### Current Situation
- As of **September 10, 2025**, United Chargers announced that it is temporarily not possible to connect their charger to a custom OCPP server other than their own.  
- This issue has been ongoing for over a month and is expected to last for about another month.  

### Error Example
The intercepted error looks like this:


In short:  
`{"configurationKey":],"unknownKey":["MeterValuesSampledData"]}` is invalid → the charger disconnects from the OCPP server.  

### Fix
This GitHub patch simply intercepts that malformed message and ignores it, allowing the charger to keep working with Home Assistant.  

---

✅ **As long as you do not update the firmware, your charger will continue to work correctly with Home Assistant.**


[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![codecov](https://codecov.io/gh/lbbrhzn/ocpp/branch/main/graph/badge.svg?token=3FRJIF5KRW)](https://codecov.io/gh/lbbrhzn/ocpp)
[![Documentation Status](https://readthedocs.org/projects/home-assistant-ocpp/badge/?version=latest)](https://home-assistant-ocpp.readthedocs.io/en/latest/?badge=latest)
[![hacs_downloads](https://img.shields.io/github/downloads/djiesr/ocpp/latest/total)](https://github.com/djiesr/ocpp/releases/latest)

![OCPP](https://github.com/home-assistant/brands/raw/master/custom_integrations/ocpp/icon.png)

This is a temporary version awaiting the necessary fixes from United Chargers for the compatibility of the Grizzl-E Smart charger with the OCPP standards used in the original version created by lbbrhzn.

From [lbbrhzn/ocpp](https://github.com/lbbrhzn/ocpp) V0.6.3, patched for **Grizzl-E Smart** charger.

Tested with the firmware: **GWM-07.027-03_GCW-10.22-05.7**

Add the integration with the default instalation.

From your charger, set the server: the ws://homeassistant.local:9000/

All other information is in the documentation you can found here [home-assistant-ocpp.readthedocs.io](https://home-assistant-ocpp.readthedocs.io)

* based on the [Python OCPP Package](https://github.com/mobilityhouse/ocpp).
* HACS compliant repository 



**💡 Tip:** If you like this project consider buying a coffee or a cocktail **to lbbrhzn**:

<a href="https://www.buymeacoffee.com/lbbrhzn" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/default-black.png" alt="Buy A Coffee To lbbrhzn" width="150px">
</a>








