
This is a tool for processing time.



# Installation

It is possible to install the tool with pip:

```
pip install xt-TimeUtils
```



# Feature

Time processing module based on *`datetime`* and *`arrow`*



# Configuration

The script itself is currently configuration free.



# Dependencies

- arrow
- datetime



# Usage

Sample usage:

```python
from xtdate_utils.xtdate_utils import TimeUtils

str_to_datetime = TimeUtils.str_to_datetime('2021-01-01', '%Y-%m-%d')
```



# Changes

**Version 0.1.3**

- Add two new interfaces(*`get_after_day`*, *`get_before_day`*)

**Version 0.1.4**

- Initial version
- Fix the error of importerror



# License

The script is released under the MIT License.The MIT License is registered with and approved by the Open Source Initiative.
