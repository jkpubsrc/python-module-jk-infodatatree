# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'bool'

General information:

* *FlexStruct type name:* `bool`
* *Input value:* Boolean value
* *Expected value type:* `bool`

Default output:

* *Description:* Outputs 'yes' or 'no'
* *Output example:* "`yes`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'bytes'

General information:

* *FlexStruct type name:* `bytes`
* *Input value:* Number of bytes
* *Expected value type:* `int`

Default output:

* *Description:* The number of bytes in human readable form
* *Output example:* "`3.45 MB`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'duration'

General information:

* *FlexStruct type name:* `duration`
* *Input value:* Number of seconds
* *Expected value type:* `int, float`

Default output:

* *Description:* Time spent in human readable form
* *Output example:* "`3 hours, 1 minute, 29 seconds`"

The following visualization flavors exist:

* "`secs`"
	* *Description:* Number of seconds spent in human readable form
	* *Output example:* "`129 seconds`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'float'

General information:

* *FlexStruct type name:* `float`
* *Input value:* Float value
* *Expected value type:* `float`

Default output:

* *Description:* The input value as provided
* *Output example:* "`3.1415927`"

The following visualization flavors exist:

* "`%0`"
	* *Description:* The float value formatted as a percent value with zero decimal digits
	* *Output example:* "`23%`"
* "`%1`"
	* *Description:* The float value formatted as a percent value with one decimal digit
	* *Output example:* "`23.4%`"
* "`%2`"
	* *Description:* The float value formatted as a percent value with two decimal digits
	* *Output example:* "`23.45%`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'float[]'

General information:

* *FlexStruct type name:* `float[]`
* *Input value:* List of float values
* *Expected value type:* `float[]`

Default output:

* *Description:* Float values separated by comma
* *Output example:* "`99.9, 4.1, 87, 7.358`"

The following visualization flavors exist:

* "`sorted`"
	* *Description:* Sorted float values separated by comma
	* *Output example:* "`4.1, 7.358, 87, 99.9`"
* "`shorten`"
	* *Description:* Shortened float value list separated by comma
	* *Output example:* "`99.9, 4.1, 87, ...`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'freq'

General information:

* *FlexStruct type name:* `freq`
* *Input value:* Frequency = Number of events per second
* *Expected value type:* `int, float`

Default output:

* *Description:* The frequency in human readable form
* *Output example:* "`3.45 GHz`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'int'

General information:

* *FlexStruct type name:* `int`
* *Input value:* Integer value
* *Expected value type:* `int`

Default output:

* *Description:* The input value as provided
* *Output example:* "`123`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'int[]'

General information:

* *FlexStruct type name:* `int[]`
* *Input value:* List of integer values
* *Expected value type:* `int[]`

Default output:

* *Description:* Integer values separated by comma
* *Output example:* "`99, 4, 87, 7`"

The following visualization flavors exist:

* "`sorted`"
	* *Description:* Sorted integer values separated by comma
	* *Output example:* "`4, 7, 87, 99`"
* "`shorten`"
	* *Description:* Shortened integer value list separated by comma
	* *Output example:* "`99, 4, 87, ...`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'secsdiff'

General information:

* *FlexStruct type name:* `secsdiff`
* *Input value:* Number of seconds
* *Expected value type:* `int, float`

Default output:

* *Description:* The difference in time
* *Output example:* "`+00:02:39`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'str'

General information:

* *FlexStruct type name:* `str`
* *Input value:* String value
* *Expected value type:* `str`

Default output:

* *Description:* The input string as provided
* *Output example:* "`abcdef`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'str[]'

General information:

* *FlexStruct type name:* `str[]`
* *Input value:* List of string values
* *Expected value type:* `str[]`

Default output:

* *Description:* String values separated by comma
* *Output example:* "`Mon, Tue, Wed, Thur, Fri`"

The following visualization flavors exist:

* "`sorted`"
	* *Description:* Sorted string values separated by comma
	* *Output example:* "`Mon, Tue, Wed, Thur, Fri`"
* "`shorten`"
	* *Description:* Shortened string value list separated by comma
	* *Output example:* "`Mon, Tue, Wed, ...`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'tempc'

General information:

* *FlexStruct type name:* `tempc`
* *Input value:* Temperature in °C
* *Expected value type:* `int, float`

Default output:

* *Description:* The temperature value in human readable form
* *Output example:* "`37.1 °C`"

There are no visualization flavors for this data type.

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'timestamp'

General information:

* *FlexStruct type name:* `timestamp`
* *Input value:* Number of seconds since Epoch
* *Expected value type:* `int, float`

Default output:

* *Description:* Returns time stamp in human readable form
* *Output example:* "`23.03.2020 12:03:59`"

The following visualization flavors exist:

* "`age`"
	* *Description:* Returns time stamp in human readable form
	* *Output example:* "`yesterday 12:03:59`"

# Data types

The following sections provide an overview about all data types supported by the data value data structure.

## Data type: 'timestamputc'

General information:

* *FlexStruct type name:* `timestamputc`
* *Input value:* Number of UTC seconds since Epoch
* *Expected value type:* `int, float`

Default output:

* *Description:* Returns time stamp in human readable form
* *Output example:* "`23.03.2020 12:03:59`"

The following visualization flavors exist:

* "`age`"
	* *Description:* Returns time stamp in human readable form
	* *Output example:* "`yesterday 12:03:59`"
