# Introduction

## Data structures representing data values

A single data value is represented by a data structure with the following fields:

* `str dt` : An identifier representing a data type.
	* There are a variety of datatypes defined. These definitions are described in section "Data types".
* `* v` : The data value itself.
	* The exact type of value stored here is not defined as this can vary.
	* As these data structures should be stored as JSON the value must be one of the following types: `(null)`, `boolean`, `int`, `float`, `string`, `list`. `dictionary` would be possible but is not used right now and therefore prohibited.
	* If a list is stored the individual list items must be of type `int`, `float` or `string`. Other types are not supported right now.
	* This field is optional. It may be present and contain `(null)` which is equivalent as if it would not be present.
* `* v0` : Equivalent to `v` but for a value that has been stored in this data structure some time ago.
	* This field is optional. It may be present and contain `(null)` which is equivalent as if it would not be present.
* `str a` : This is an alert marker for this data value.
	* If this field is present it must contain one of the following values:
		* `warn` : Which means "warning" and marks this data value as somehow problematic.
			* If displayed it should be highlighted as this value should be kept in focus.
		* `err` : Which means "error" and marks this data value as problematic.
			* If displayed it must be highlighted as this value requires attention.
		* `crit` : Which means "critical" and marks this data value as very problematic.
			* If displayed it must be highlighted as this value requires attention.
	* This field is optional.

## Data types

For details about the data types supported, see: `Data Types (autogenerated)`.











