import pytest

from config import Config, JsonConfig

if __name__ == '__main__':
    app_mode = JsonConfig.get_data('APP_MODE')
    JsonConfig.set_data('APP_MODE', Config.APP_MODE_TESTING)
    pytest.main()
    JsonConfig.set_data('APP_MODE', app_mode)
