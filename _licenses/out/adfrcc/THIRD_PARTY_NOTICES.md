# Third-party notices

ADFRcc (Python package `adfrcc`) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## NLopt C++ interface (`nlopt.hpp`)

- **Where:** `ADFRcc/_adfrcc.so` (and its copy `ADFRcc/_adfrcc.cpython-37m-x86_64-linux-gnu.so`)
- **Copyright:** © 2007–2011 Massachusetts Institute of Technology
- **License:** MIT License
- **License text:**

```
/* Copyright (c) 2007-2011 Massachusetts Institute of Technology
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
 */
```

- **Source:** https://github.com/stevengj/nlopt
- The inline code of the header `nlopt.hpp` is compiled into the extension. The extension loads the NLopt library (`libnlopt.so.0`, GNU LGPL 2.1 or later) at run time; that library is distributed with the adfr package, whose notices list it.
