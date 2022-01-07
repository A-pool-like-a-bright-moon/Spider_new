var n = {}

function p(e, t) {
var n = (65535 & e) + (65535 & t);
return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}
function a(e, t, n, o, i, r) {
return p((s = p(p(t, e), p(o, r))) << (a = i) | s >>> 32 - a, n);
var s, a
}
function l(e, t, n, o, i, r, s) {
return a(t & n | ~t & o, e, t, i, r, s)
}
function m(e, t, n, o, i, r, s) {
return a(t & o | n & ~o, e, t, i, r, s)
}
function f(e, t, n, o, i, r, s) {
return a(t ^ n ^ o, e, t, i, r, s)
}
function g(e, t, n, o, i, r, s) {
return a(n ^ (t | ~o), e, t, i, r, s)
}
function c(e, t) {
e[t >> 5] |= 128 << t % 32,
e[14 + (t + 64 >>> 9 << 4)] = t;
var n, o, i, r, s, a = 1732584193,
c = -271733879,
u = -1732584194,
d = 271733878;
for (n = 0; n < e.length; n += 16) a = l(o = a, i = c, r = u, s = d, e[n], 7, -680876936),
d = l(d, a, c, u, e[n + 1], 12, -389564586),
u = l(u, d, a, c, e[n + 2], 17, 606105819),
c = l(c, u, d, a, e[n + 3], 22, -1044525330),
a = l(a, c, u, d, e[n + 4], 7, -176418897),
d = l(d, a, c, u, e[n + 5], 12, 1200080426),
u = l(u, d, a, c, e[n + 6], 17, -1473231341),
c = l(c, u, d, a, e[n + 7], 22, -45705983),
a = l(a, c, u, d, e[n + 8], 7, 1770035416),
d = l(d, a, c, u, e[n + 9], 12, -1958414417),
u = l(u, d, a, c, e[n + 10], 17, -42063),
c = l(c, u, d, a, e[n + 11], 22, -1990404162),
a = l(a, c, u, d, e[n + 12], 7, 1804603682),
d = l(d, a, c, u, e[n + 13], 12, -40341101),
u = l(u, d, a, c, e[n + 14], 17, -1502002290),
a = m(a, c = l(c, u, d, a, e[n + 15], 22, 1236535329), u, d, e[n + 1], 5, -165796510),
d = m(d, a, c, u, e[n + 6], 9, -1069501632),
u = m(u, d, a, c, e[n + 11], 14, 643717713),
c = m(c, u, d, a, e[n], 20, -373897302),
a = m(a, c, u, d, e[n + 5], 5, -701558691),
d = m(d, a, c, u, e[n + 10], 9, 38016083),
u = m(u, d, a, c, e[n + 15], 14, -660478335),
c = m(c, u, d, a, e[n + 4], 20, -405537848),
a = m(a, c, u, d, e[n + 9], 5, 568446438),
d = m(d, a, c, u, e[n + 14], 9, -1019803690),
u = m(u, d, a, c, e[n + 3], 14, -187363961),
c = m(c, u, d, a, e[n + 8], 20, 1163531501),
a = m(a, c, u, d, e[n + 13], 5, -1444681467),
d = m(d, a, c, u, e[n + 2], 9, -51403784),
u = m(u, d, a, c, e[n + 7], 14, 1735328473),
a = f(a, c = m(c, u, d, a, e[n + 12], 20, -1926607734), u, d, e[n + 5], 4, -378558),
d = f(d, a, c, u, e[n + 8], 11, -2022574463),
u = f(u, d, a, c, e[n + 11], 16, 1839030562),
c = f(c, u, d, a, e[n + 14], 23, -35309556),
a = f(a, c, u, d, e[n + 1], 4, -1530992060),
d = f(d, a, c, u, e[n + 4], 11, 1272893353),
u = f(u, d, a, c, e[n + 7], 16, -155497632),
c = f(c, u, d, a, e[n + 10], 23, -1094730640),
a = f(a, c, u, d, e[n + 13], 4, 681279174),
d = f(d, a, c, u, e[n], 11, -358537222),
u = f(u, d, a, c, e[n + 3], 16, -722521979),
c = f(c, u, d, a, e[n + 6], 23, 76029189),
a = f(a, c, u, d, e[n + 9], 4, -640364487),
d = f(d, a, c, u, e[n + 12], 11, -421815835),
u = f(u, d, a, c, e[n + 15], 16, 530742520),
a = g(a, c = f(c, u, d, a, e[n + 2], 23, -995338651), u, d, e[n], 6, -198630844),
d = g(d, a, c, u, e[n + 7], 10, 1126891415),
u = g(u, d, a, c, e[n + 14], 15, -1416354905),
c = g(c, u, d, a, e[n + 5], 21, -57434055),
a = g(a, c, u, d, e[n + 12], 6, 1700485571),
d = g(d, a, c, u, e[n + 3], 10, -1894986606),
u = g(u, d, a, c, e[n + 10], 15, -1051523),
c = g(c, u, d, a, e[n + 1], 21, -2054922799),
a = g(a, c, u, d, e[n + 8], 6, 1873313359),
d = g(d, a, c, u, e[n + 15], 10, -30611744),
u = g(u, d, a, c, e[n + 6], 15, -1560198380),
c = g(c, u, d, a, e[n + 13], 21, 1309151649),
a = g(a, c, u, d, e[n + 4], 6, -145523070),
d = g(d, a, c, u, e[n + 11], 10, -1120210379),
u = g(u, d, a, c, e[n + 2], 15, 718787259),
c = g(c, u, d, a, e[n + 9], 21, -343485551),
a = p(a, o),
c = p(c, i),
u = p(u, r),
d = p(d, s);
return [a, c, u, d]
}
function u(e) {
var t, n = "";
for (t = 0; t < 32 * e.length; t += 8) n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
return n
}
function d(e) {
var t, n = [];
for (n[(e.length >> 2) - 1] = void 0, t = 0; t < n.length; t += 1) n[t] = 0;
for (t = 0; t < 8 * e.length; t += 8) n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
return n
}
function o(e) {
var t, n, o = "0123456789abcdef",
i = "";
for (n = 0; n < e.length; n += 1) t = e.charCodeAt(n),
i += o.charAt(t >>> 4 & 15) + o.charAt(15 & t);
return i
}
function i(e) {
return unescape(encodeURIComponent(e))
}
function r(e) {
return u(c(d(t = i(e)), 8 * t.length));
var t
}
function s(e, t) {
return function(e, t) {
    var n, o, i = d(e),
    r = [],
    s = [];
    for (r[15] = s[15] = void 0, 16 < i.length && (i = c(i, 8 * e.length)), n = 0; n < 16; n += 1) r[n] = 909522486 ^ i[n],
    s[n] = 1549556828 ^ i[n];
    return o = c(r.concat(d(t)), 512 + 8 * t.length),
    u(c(s.concat(o), 640))
} (i(e), i(t))
}
function getpwd(e, t, n) {
return t ? n ? s(t, e) : o(s(t, e)) : n ? r(e) : o(r(e))
}