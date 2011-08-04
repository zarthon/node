{
  'targets': [
    {
      'target_name': 'http_parser',
      'type': 'static_library',
      'include_dirs': [ '.' ],
      'direct_dependent_settings': {
        'include_dirs': [ '.' ],
      },
      'defines': [ 'HTTP_PARSER_STRICT=0' ],
      'sources': [
        './http_parser.c',
      ],
    },

    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [ 'http_parser' ],
      'sources': [ 'test.c' ]
    }
  ]
}

