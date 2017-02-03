{
  'variables': {
    'target_arch%': '<!(node preinstall.js --print-arch)>'
  },
  'targets': [
    {
      'target_name': 'sodium',
      'include_dirs' : [
        "<!(node -e \"require('nan')\")",
        'deps/libsodium/src/libsodium/include'
      ],
      'sources': [
        'binding.cc',
        'src/crypto_generichash_wrap.cc',
        'src/crypto_onetimeauth_wrap.cc',
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-g',
          '-O3',
        ]
      },
      'cflags': [
        '-g',
        '-O3',
      ],
      'libraries': [
        '<!(node preinstall.js --print-lib)'
      ],
      'conditions': [
        ['OS=="linux"', {
          'link_settings': {
            'libraries': [ "-Wl,-rpath=\\$$ORIGIN/"]
          }
        }],
      ],
    }
  ]
}
