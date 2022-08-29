- [ZDP帧格式](#zdp帧格式)
  - [Transaction sequence number](#transaction-sequence-number)
  - [Transaction data](#transaction-data)
- [典型ZDP帧](#典型zdp帧)
  - [Client Services](#client-services)
    - [Device and Service Discovery](#device-and-service-discovery)
      - [Node_Desc_req](#node_desc_req)
      - [Match_Desc_req](#match_desc_req)
      - [Device_annce](#device_annce)
    - [Network Management](#network-management)
      - [Mgmt_Permit_Joining_req](#mgmt_permit_joining_req)
  - [Server Services](#server-services)
    - [Device and Service Discovery](#device-and-service-discovery-1)
      - [Node_Desc_rsp](#node_desc_rsp)
      - [Match_Desc_rsp](#match_desc_rsp)
- [ZDP Enumeration Description](#zdp-enumeration-description)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

>参考zigbee specification -> 2.4 The ZigBee Device Profile

> All ZDP commands shall be transmitted via the <font color=red>APS data service</font> and shall be formatted according to the ZDP frame structure
>
> <font color=red>note</font>: ZDP是[APS Data Frame](APS#data-frame)的Payload部分

## ZDP帧格式

| Octets:1                                                     | Variable                                  |
| ------------------------------------------------------------ | ----------------------------------------- |
| [Transaction sequence number](#zdp-transaction-sequence-number) | [Transaction data](#zdp-transaction-data) |

### Transaction sequence number

If a device sends a ZDP request command that [requires a response](#), the target device shall respond with the relevant ZDP response command and include the transaction sequence number contained in the original request command.

<font color=red>NOTE: 同一类型的ZDP帧sequence number不变，当target收到需要回应的ZDP包，sequence number相应位和接收的一样。</font>

### Transaction data

The transaction data field has a variable length and contains the data for the individual ZDP transaction.

<font color=red>NOTE: 根据APS不同的[Cluster Identifier](#aps-cluster-identifier)，有不同的Transaction data格式。</font>具体查看[典型ZDP帧](#典型zdp帧)。

## 典型ZDP帧

> 跳转内容均为[Transaction data](#zdp-transaction-data)。图中，M表示"MUST"，O表示"OPTION"

| Cluster ID   | Services                                                     | Type                                                         | Client Transmission | Server Processing |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------- | ----------------- |
| ***0x0000*** | NWK_addr_req                                                 | [Device and Service Discovery Client Services](#zdp-client-services-device-and-service-discovery) |                     |                   |
|              | IEEE_addr_req                                                |                                                              |                     |                   |
| ***0x0002*** | [Node_Desc_req](#zdp-client-services-device-and-service-discovery-node_desc_req) |                                                              | M                   | M                 |
|              | Power_Desc_req                                               |                                                              |                     |                   |
|              | Simple_Desc_req                                              |                                                              |                     |                   |
|              | Active_EP_req                                                |                                                              |                     |                   |
| ***0x0006*** | [Match_Desc_req](#zdp-client-services-device-and-service-discovery-match_desc_req) |                                                              | O                   | M                 |
|              | Complex_Desc_req                                             |                                                              |                     |                   |
|              | User_Desc_req                                                |                                                              |                     |                   |
|              |                                                              |                                                              |                     |                   |
|              |                                                              |                                                              |                     |                   |
| ***0x0013*** | [Device_annce](#zdp-client-services-device-and-service-discovery-device_annce) |                                                              | O                   | M                 |
|              |                                                              |                                                              |                     |                   |
|              |                                                              |                                                              |                     |                   |
| ***0x0036*** | [Mgmt_Permit_Joining_req](#zdp-client-services-network-management-mgmt_permit_joining_req) | [Network Management Client Services](#zdp-client-services-network-management) | O                   | M                 |
|              |                                                              |                                                              |                     |                   |
| ***0x8002*** | [Node_Desc_rsp](#zdp-server-services-device-and-service-discovery-node_desc_rsp) | [Device and Service Discovery Server Services](#zdp-server-services-device-and-service-discovery) |                     | M                 |

### Client Services

#### Device and Service Discovery



##### Node_Desc_req

* **format**

  | Octets          | 2                           |
  | --------------- | --------------------------- |
  | **Name**        | ***NWKAddrOfInterest***     |
  | **Type**        | Device Address              |
  | **Valid Range** | 16-bit NWK address          |
  | **Description** | NWK address for the request |

* **description**

  The Node_Desc_req command is generated from <font color=red>a local device wishing to inquire as to the node descriptor of a remote device</font>. This command shall be unicast either to the remote device itself or to an alternative device that contains the discovery information of the remote device.

* **Receipt**

  Upon receipt of this command, the recipient device shall process the command and generate a [Node_Desc_rsp command](#zdp-server-services-device-and-service-discovery-node_desc_rsp) in response.

##### Match_Desc_req

| Octets          | 2                            | 2                                                   | 1                                                            | Variable                                                     | 1                                                            | Variable                                                     |
| --------------- | ---------------------------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Name**        | *NWKAddrOfInterest*          | *ProfileID*                                         | *NumInClusters*                                              | *InClusterList*                                              | *NumOutClusters*                                             | *OutClusterList*                                             |
| **Type**        | Device Address               | Integer                                             | Integer                                                      |                                                              | Integer                                                      |                                                              |
| **Valid Range** | ***16-bit NWK address***     | ***0x0000~0xffff***                                 | ***0x00~0xff***                                              | ***2 *NumInClusters(bytes)***                                | ***0x00~0xff***                                              | ***2*NumOutClusters(bytes)***                                |
| **Description** | NWK address for the request. | ==MYQ==Profile ID to be matched at the destination. | The number of Input Clusters provided for matching within the InClusterList | List of Input [ClusterIDs](#zcl-cluster-list) to be used for matching the InClusterList is the desired list to be matched by the Remote Device (the elements of the InClusterList are the supported output clusters of the Local Device) | The number of Output Clusters provided for matching within OutClusterList. | List of Output [ClusterIDs](#zcl-cluster-list)  to be used for matching; the OutClusterList is the desired list to be matched by the Remote Device (the elements of the OutClusterList are the supported input clusters of the Local Device). |

##### Device_annce

* **format**

| Octets          | 2                                | 8                                 | 1                                                            |
| --------------- | -------------------------------- | --------------------------------- | ------------------------------------------------------------ |
| **Name**        | ***NWK Addr***                   | ***IEEEAddr***                    | ***Capability***                                             |
| **Type**        | Device Address                   | Device Address                    | Bitmap                                                       |
| **Valid Range** | 16-bit NWK address               | 64-bit IEEE address               | [MAC capability flags](#zigbee-descriptors-node-mac-capability-flags) |
| **Description** | NWK address for the Local Device | IEEE address for the Local Device | Capability of the local device                               |

* **description**

  The Device_annce is provided to enable ZigBee devices on the network to <font color=red>notify other ZigBee devices that the device has joined or re-joined the network</font>, identifying the device’s 64-bit IEEE address and new 16-bit NWK address, and <font color=red>informing the Remote Devices of the capability of the ZigBee device. </font>

* **invoke**

  This command shall be invoked for all ZigBee end devices upon join or rejoin. This command may also be invoked by ZigBee routers upon join or rejoin as part of NWK address conflict resolution. <font color=red>The destination addressing on this primitive is broadcast to all devices</font> for which [macRxOnWhenIdle](#macrxonwhenidle) = TRUE

* **Receipt**

  Upon receipt, the Remote Device shall use the IEEEAddr in the message to find a match with any other IEEE address held in the Remote Device. If a match is detected, the Remote Device shall update the nwkAddressMap attribute of the NIB with the updated NWKAddr corresponding to the IEEEAddr received. 
  The Remote Device shall also use the NWKAddr in the message to find a match with any other 16-bit NWK address held in the Remote Device, even if the IEEEAddr field in the message carries the value of 0xffffffffffffffff. If a match is detected for a device with an IEEE address other than that indicated in the IEEEAddr field received, then this entry shall be marked as not having a known valid 16-bit NWK address.



#### Network Management



##### Mgmt_Permit_Joining_req

> Only devices that are either the <font color=red>ZigBee coordinator</font> or a <font color=red>ZigBee router</font> shall attempt to permit devices to join the network.

* **format**

  | Octets          | 1                                       | 1                                                            |
  | --------------- | --------------------------------------- | ------------------------------------------------------------ |
  | **Name**        | ***PermitDuration***                    | ***TC_Significance***                                        |
  | **Type**        | Integer                                 | Boolean Integer                                              |
  | **Valid Range** | ***0x00-0xfe***                         | ***0x01***                                                   |
  | **Description** | The status of the Node_Desc_req command | This field shall always have a value of 1, indicating a request to change the Trust Center policy. If a frame is received with a value of 0, it shall be treated as having a value of 1. |

* **description**

  * ***PermitDuration*** == ***0x00*** : the NLME sets the MAC PIB attribute [*macAssociationPermit*](#macassociationpermit) to ***FALSE*** . 
  * ***PermitDuration*** = ***0xff*** : the NLME sets [*macAssociationPermit*](#macassociationpermit)  to ***TRUE***.
  * ***PermitDuration*** = ***0x01~0xfe*** : the NLME sets [*macAssociationPermit*](#macassociationpermit) to ***TRUE***. Following the receipt of the MLME-SET.confirm primitive, the NLME starts a timer to expire after ***PermitDuration*** seconds. The NLME shall then start a timer to expire after the specified duration. On expiration of this timer, the NLME shall set the [*macAssociationPermit*](#macassociationpermit) to ***FALSE.***

* **invoke**

  The Mgmt_Permit_Joining_req is generated from a Local Device requesting that a remote device or devices allow or disallow association.The Mgmt_Permit_Joining_req is generated by a management application or commissioning tool which directs the request to a remote device(s) where the <font color=red>NLME-PERMIT-JOINING.request</font> is executed using the ***PermitDuration*** parameter supplied by Mgmt_Permit_Joining_req.

* **Receipt**



### Server Services

#### Device and Service Discovery



##### Node_Desc_rsp

<font color=red>response to a [Node_Desc_req](#zdp-client-services-device-and-service-discovery-node_desc_req) directed to the remote device</font>. 

| Octets          | 1                                                            | 2                            | Variable                                                     |
| --------------- | ------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ |
| **Name**        | ***Status***                                                 | ***NWKAddrOfInterest***      | ***Node Descriptor***                                        |
| **Type**        | Integer                                                      | Device Address               | Node Descriptor                                              |
| **Valid Range** | [***SUCCESS***](#zdp-enumeration-description-success)<br/>[***DEVICE_NOT_FOUND***](#zdp-enumeration-description-device_not_found)<br/>[***INV_REQUESTTYPE***](#zdp-enumeration-description-inv_requesttype)<br/>[***NO_DESCRIPTOR***](#zdp-enumeration-description-no_descriptor) | 16-bit NWK address           | = [***Node Descriptor***](#zigbee-descriptors-node) : ***Status==SUCCESS***<br />= ***NONE*** : otherwise |
| **Description** | The status of the Node_Desc_req command                      | NWK address for the request. |                                                              |

##### Match_Desc_rsp

<font color=red>response to a [Match_Desc_req](#zdp-client-services-device-and-service-discovery-match_desc_req) directed to the remote device</font>. 

| Octets          | 1                                                            | 2                            | 1                                                            | Variable                                                  |
| --------------- | ------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| **Name**        | *Status*                                                     | *NWKAddrOfInterest*          | *Match Length*                                               | *Match List*                                              |
| **Type**        | Integer                                                      | Device Address               |                                                              |                                                           |
| **Valid Range** | [***SUCCESS***](#zdp-enumeration-description-success)<br/>[***DEVICE_NOT_FOUND***](#zdp-enumeration-description-device_not_found)<br/>[***INV_REQUESTTYPE***](#zdp-enumeration-description-inv_requesttype)<br/>[***NO_DESCRIPTOR***](#zdp-enumeration-description-no_descriptor) | ***16-bit NWK address***     | ***0x00-0xff***                                              |                                                           |
| **Description** | The status of the Match_Desc_req command                     | NWK address for the request. | The count of endpoints on the Remote Device that match the request criteria. | List of bytes each of which represents an 8-bit endpoint. |



## ZDP Enumeration Description

| Enumeration                                                  | Value     | Description                                                  |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| ***SUCCESS*** | 0x00      | The requested operation or transmission was completed successfully. |
| −                                                            | 0x01-0x7f | Reserved.                                                    |
| ***INV_REQUESTTYPE*** | 0x80      | The supplied request type was invalid.                       |
| ***DEVICE_NOT_FOUND*** | 0x81      | The requested device did not exist on a device following a child descriptor request to a parent. |
| ***INVALID_EP*** | 0×82      | The supplied endpoint was equal to 0x00 or 0xff.             |
| ***NOT_ACTIVE*** | 0×83      | The requested endpoint is not described by a simple descriptor. |
| ***NOT_SUPPORTED*** | 0×84      | The requested optional feature is not supported on the target device. |
| ***TIMEOUT*** | 0×85      | A timeout has occurred with the requested operation.         |
| ***NO_MATCH*** | 0×86      | The end device bind request was unsuccessful due to a failure to match any suitable clusters. |
| −                                                            | 0×87      | Reserved.                                                    |
| ***NO_ENTRY*** | 0 x 88    | The unbind request was unsuccessful due to the coordinator or source device not having an entry in its binding table to unbind. |
| ***NO_DESCRIPTOR***                                          | 0×89      | A child descriptor was not available following a discovery request to a parent. |
| ***INSUFFICIENT_SPACE***                                     | 0x8a      | The device does not have storage space to support the requested operation. |
| ***NOT_PERMITTED***                                          | 0x8b      | The device is not in the proper state to support the requested operation. |
| ***TABLE_FULL***                                             | 0x8c      | The device does not have table space to support the operation. |
| ***NOT_AUTHORIZED***                                         | 0x8d      | The device has rejected the command due to security restrictions. |
| ***DEVICE_BINDING_TABLE_FULL***                              | 0x8e      | The device does not have binding table space to support the operation. |
| ***INVALID_INDEX***                                          | 0x8f      | The index in the received command is out of bounds.          |
| −                                                            | 0x90-0xff | Reserved.                                                    |
