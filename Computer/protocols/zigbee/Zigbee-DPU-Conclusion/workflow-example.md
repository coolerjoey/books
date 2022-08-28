## Lighting

> ZC: Zigbee Coordinator
>
> ZR : Zigbee Router 
>
> ZED : Zigbee EndDevice

| index | dir                                 | Command                                                      | Layer | note                                     |
| ----- | ----------------------------------- | ------------------------------------------------------------ | ----- | ---------------------------------------- |
| 1     | ZR &rarr; ZC                        | [Beacon Request](MAC#beacon-request)                         | MAC   |                                          |
|       | ZR &larr; ZC              | [Beacon](MAC#beacon-frame)                                   | MAC   |                                          |
|       | ZR &rarr; ZC                        | [Association Request](MAC#association-request)               | MAC   |                                          |
|       | ZR &larr; ZC              | [Ack](MAC#ack-frame)                                         | MAC   |                                          |
|       | ZR &rarr; ZC                        | [Data Request](MAC#data-request)                             | MAC   |                                          |
|       | ZR &larr; ZC              | [Ack](MAC#ack-frame)                                         | MAC   |                                          |
|       | ZR &larr; ZC              | [Association Response](MAC#association-response)             | MAC   | 给设备分配短地址                         |
|       | ZR &rarr; ZC             | [Ack](MAC#ack-frame)                                         | MAC   |                                          |
|       | ZR &larr; ZC              | [Transport Key-Network Key](APS#aps-transport-key-network-key) | APS   | 给设备发送Network Key                    |
|       | ZR &rarr; ZC             | [Ack](MAC#ack-frame)                                         | MAC   |                                          |
|       | ZR &rarr; **Broadcast**  | [Device Announcement](ZDP#device-annce) | ZDP   | 广播通知设备已入网                       |
|       | ZC &rarr; **Broadcast**  | [Device Announcement](ZDP#device-annce) |       | ZC转发上一条组网通知?         |
|       | ZR &rarr; ZC             | [Node Descriptor Request](ZDP#node_desc_req) | ZDP   | 向Coordinator获取节点描述符              |
|       | ZR &larr; ZC              | [APS ACK](APS#acknowledgement-frame)                     | APS   |                                          |
|       | ZR &larr; ZC              | [Node Descriptor Response](ZDP#node_desc_rsp) | ZDP   | Coordinator发送节点描述符                |
|       | ZR &rarr; ZC             | [APS ACK](APS#acknowledgement-frame)                    | APS   |                                          |
|       | ZR &rarr; ZC             | [Request Key-Trust Center Link Key](APS#request-key) | APS | 向Coordinator获取Trust Center Link Key   |
|       | ZR &larr; ZC              | [Transport Key-Trust Center Link Key](APS#transport-key-trust-center-link-key) | APS | Coordinator发送Trust Center Link Key     |
|       | ZR &rarr; ZC             | [Verify Key-Trust Center Link Key](APS#verify-key) | APS | 和Coordinator确认Trust Center Link Key   |
|       | ZR &larr; ZC              | [Confirm Key-Trust Center Link Key](APS#confirm-key) | APS | Coordinator确认Trust Center Link Key正确 |
|       | ZR &rarr; **Broadcast**  | [Permit Join Request](ZDP#permit_joining_req) | ZDP   | 广播可以加入该Rouer的网络                |
|       | ZR &rarr; **Broadcast**  | [Link Status](NWK#link-status)          | NWK   | Router广播连接信息                       |
|       | ZC &rarr; **Broadcast**  | [Link Status](NWK#link-status)             | NWK   | Coordinator广播连接信息                  |
| ...   | ZED &harr; ZC          |                                                              |       | ZED设备入网                              |
|       | ZED &rarr; **Broadcast** | [Match Description Request](ZDP#match_desc_req) | ZDP   | ZED设备对Router设备配对请求              |
|       | ZR &rarr; ZED             | [Match Description Response](ZDP#match_desc_rsp) | ZDP   | ZR相应ZED配对请求                        |
|       | ZR &larr; ZED              | [APS ACK](APS#acknowledgement-frame)                     | APS   |                                          |
|       | ZR &larr; ZED              | [ZCL OnOff](ZCL#onoff)                      | ZCL   | ZED向ZR发送On/Off指令                    |
|       | ZR &rarr; ZED             | [APS ACK](APS#acknowledgement-frame)                     | APS   |                                          |
|       | ZR &larr; ZED              | [ZCL Level Control](ZCL#level-control)       | ZCL   | ZED向ZR发送Level调节指令                 |
|       | ZR &rarr; ZED             | [APS ACK](APS#acknowledgement-frame)                   | APS   |                                          |

# 