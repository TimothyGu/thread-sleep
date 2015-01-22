{
  "targets": [
    {
      "target_name": "thread_sleep",
      "sources": [
        "thread_sleep.cc"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "conditions": [
          ['OS=="solaris"', {
            'cflags': [ '-pthreads' ],
          }],
          ['OS not in "solaris android"', {
            'cflags': [ '-pthread' ],
          }],
          [ 'OS=="mac"', {
              "xcode_settings": {
                  'OTHER_CPLUSPLUSFLAGS' : ['-stdlib=libc++', '-v'],
                  'OTHER_LDFLAGS': ['-stdlib=libc++'],
                  'MACOSX_DEPLOYMENT_TARGET': '10.7',
                  'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
              }
          }]
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
