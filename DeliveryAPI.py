import http.client

conn = http.client.HTTPSConnection("api.ncr.com")

payload = "{\"driverTip\":2,\"dropoffContact\":{\"businessName\":\"NC Corp\",\"firstName\":\"George\"," \
          "\"instructions\":\"This guy is really awesome\",\"lastName\":\"Burdell\",\"phoneNumber\":\"4048675309\"," \
          "\"smsOptIn\":false},\"externalOrderId\":\"ABC123\",\"pickupContact\":{\"businessName\":\"NCR Corp\"," \
          "\"firstName\":\"George\",\"instructions\":\"This guy is really awesome\",\"lastName\":\"Burdell\"," \
          "\"phoneNumber\":\"4048675309\"},\"quoteId\":\"String\",\"readyForPickup\":false,\"totals\":[{" \
          "\"totalId\":\"String\",\"type\":\"Net\",\"value\":18.9}]} "

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'nep-organization': "hackGT",
    'nep-enterprise-unit': "blahblah",
    'Content-Type': "application/json"
}

conn.request("POST", "//delivery/v1/deliveries", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

headers = {
    'accept': "application/json",
    'nep-organization': "SOME_STRING_VALUE"
    }

conn.request("GET", "//delivery/v1/deliveries/ABC123", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))