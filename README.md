## hass-neeo

NEEO custom component for Home Assistant

### Features

- Recipes as switches

### Installation

1. Copy all files into `<config_dir>/custom_components`
2. Add the following into your `configuration.yaml`
    ```yaml
    neeo:
      host: <host>
    ```
    - Replace `<host>` with the IP address or hostname of your NEEO brain.

3. Restart home assistant
