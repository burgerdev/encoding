# Encoding

This repo contains a few simple codec utilities that are hard to come by on a standard POSIX system.
The common theme is that they process data from stdin and write the result to stdout, and that they have a `-d` option to convert back.

```console
$ echo 123 | hex
3132330a
$ echo 123 | hex | hex -d
123
```

## `hex`

`hex` encodes data into hexadecimal.
I can never remember which of `od`, `xdd` or `hexdump` is standardized, and neither what the arguments are to not print any decoration.
Also, the conversion from hex to octets is missing entirely.

## `base64_urlsafe`

I have a project which uses URL-safe base64 encoding, and it's a pain to create with `base64` and `sed`.
Also, you have to remember what the specified URL-safe characters are and which characters they replace.

