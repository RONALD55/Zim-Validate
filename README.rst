============
zim-validate
============
.. image:: https://img.shields.io/pypi/v/country_list.svg
        :target: https://pypi.org/project/zim-validate

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/RONALD55/Zim-Validate

Features
--------

-  This is package to assist developers to validate zimbabwean driver's license numbers, vehicle registration numbers, mobile numbers for Telecel,Econet,Netone and any other valid zim number registered under the major MNOs,Zim passports, national IDs among other things. Visit the project homepage for further information on how to use the package.



Installation
------------

To can install the zim_validate package open shell or terminal and run::

    pip install zim_validate

Usage
-----

Validate National ID:

If dashes are mandatory the ID will be in the format `12-3456789-X-01`
If the `dashes` are not mandatory the format will be `123456789X01`

Note parameter `dashes`: (Optional) If you want to make dashes compulsory on the input string

.. code-block:: python

    from zim_validate import national_id
    print(national_id("12-3456789-X-01",dashes=True))


Validate Passport:

All Zimbabwean passports are in the format AB123456

.. code-block:: python

    from zim_validate import passport
    print(passport("AB123456"))

Validate ID or passport:

All Zimbabwean passports are in the format `AB123456`
If dashes are mandatory the ID will be in the format `12-3456789-X-01`
If the `dashes` are not mandatory the format will be `123456789X01`

.. code-block:: python

    from zim_validate import id_or_passport
    print(id_or_passport("12-3456789-X-01",dashes=True))

Validate Telecel Numbers:

This can be used to check if the given mobile number is a valid Telecel number.
Pass the optional parameter `prefix` you want to make the prefix 263 mandatory

.. code-block:: python

    from zim_validate import telecel_number
    print(telecel_number("263735111111",prefix=True))


Validate Econet Numbers:

This can be used to check if the given mobile number is a valid Econet number.
Pass the optional parameter `prefix` you want to make the prefix 263 mandatory

.. code-block:: python

    from zim_validate import econet_number
    print(econet_number("263775111111",prefix=True))

Validate Netone Numbers:

This can be used to check if the given mobile number is a valid Netone number.
Pass the optional parameter `prefix` you want to make the prefix 263 mandatory

.. code-block:: python

    from zim_validate import netone_number
    print(netone_number("263715111111",prefix=True))

Validate Any Number from Telecel,Econet,Netone among other MNOs:

This can be used to check if the given mobile number is a valid Telecel,Econet or Netone number.
Pass the optional parameter `prefix` you want to make the prefix 263 mandatory

.. code-block:: python

    from zim_validate import mobile_number
    print(mobile_number("263782123345",prefix=True))

Validate Drivers License:

All Zimbabwean drivers licenses are in the format `111111AB`
Pass the optional parameter `space` if you want a space between the first 6 numbers and the last two letters

.. code-block:: python

    from zim_validate import license_number
    print(license_number("111111AB",space=False))

Validate Zim Vehicle Registration Number:

All Zimbabwean number plates are in the format `ABC1234`
Pass the optional parameter `space` if you want a space between the first three letters and the preceding letters numbers

.. code-block:: python

    from zim_validate import number_plate
    print(number_plate("ABF4495",space=False))

Bonus :Password:

Validate password to contain at at least one upper case,at least one lower case,at least one digit, at least one special character, minimum length 8

.. code-block:: python

    from zim_validate import password
    print(password("Password@1"))

License
-------

The project is licensed under the MIT license.
