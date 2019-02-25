## hass-neeo

NEEO custom component for Home Assistant

### Features

- Recipes as switches

### Installation

1. Copy the `neeo` folder into `<config_dir>/custom_components`
2. Add the following into your `configuration.yaml`
    ```yaml
    neeo:
      host: <host>
    ```
    - Replace `<host>` with the IP address or hostname of your NEEO brain.

3. Restart Home Assistant

## Support for Custom Updater

You can use [Custom Updater](https://github.com/custom-components/custom_updater) to track versions of this component. Once you have installed it, add the following to your configuration.

```yaml
custom_updater:
  track:
    - components
  component_urls:
    - https://raw.githubusercontent.com/vinteo/hass-neeo/master/custom_components.json

```