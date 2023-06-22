# Tagup Changelog

## 2023-06-22
- Removed the use of the `expressionInterpreter` when rendering Vega Lite charts. Using this renderer exposes a bug where a specified x-domain results in charts not rendering correctly. See these threads for more details: https://discuss.streamlit.io/t/time-axis-with-custom-scale/33524 https://github.com/vega/vega/issues/3632
- Pinned `wheel` to 0.40.0 to fix a build error
