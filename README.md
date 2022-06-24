# Listing files to JSON output
`Usage: list_files_json.py -p PATH -m MASK (pattern for search files default: all) -i INDEX (index  of array)`

Examples:
`list_files_json.py -p /home/sach3000/arch -m "Youfile*gz;Myfile*gz"`

```
[
  {
    "name": "Youfile11.gz",
    "path": "/home/sach3000/arch/1/Youfile11.gz",
    "size": 554009693,
    "atime": "2022-06-24 02:35:47",
    "mtime": "2022-06-24 02:35:17",
    "ctime": "2022-06-24 02:35:47",
    "ats": 1656016547,
    "owner": "sach3000",
    "group": "sach3000"
  },
  {
    "name": "Youfile12.gz",
    "path": "/home/sach3000/arch/2/Youfile12.gz",
    "size": 554009693,
    "atime": "2022-06-25 02:35:47",
    "mtime": "2022-06-25 02:35:17",
    "ctime": "2022-06-25 02:35:47",
    "ats": 1656016547,
    "owner": "sach3000",
    "group": "sach3000"
  },
  {
    "name": "Myfile12.gz",
    "path": "/home/sach3000/arch/1/Myfile12.gz",
    "size": 3007,
    "atime": "2022-06-24 02:37:38",
    "mtime": "2022-06-24 02:35:34",
    "ctime": "2022-06-24 02:37:38",
    "ats": 1656016658,
    "owner": "sach3000",
    "group": "sach3000"
  }
]

```

`list_files_json.py -p /home/sach3000/arch -m "Youfile*gz" -i -1 `

```
[
  {
    "name": "Youfile12.gz",
    "path": "/home/sach3000/arch/2/Youfile12.gz",
    "size": 554009693,
    "atime": "2022-06-25 02:35:47",
    "mtime": "2022-06-25 02:35:17",
    "ctime": "2022-06-25 02:35:47",
    "ats": 1656016547,
    "owner": "sach3000",
    "group": "sach3000"
  }
]
```


Requirements: Python > 3.6
