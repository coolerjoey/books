# Ӧ�ò�
## ����Ӧ�ò�Э��
| Ӧ�� | Ӧ�ò�Э�� | �����Э�� |
| :--- | :--- | :---: |
| ����ת�� | DNS (����ϵͳ) | [UDP](#udp) |
| �ļ����� | TFTP (���ļ�����Э��) | [UDP](#udp) |
| ·��ѡ��Э�� | RIP (·����ϢЭ��) | [UDP](#udp) |
| IP ��ַ���� | DHCP (��̬��������Э��) | [UDP](#udp) |
| ������� | SNMP (���������Э��) | [UDP](#udp) |
| Զ���ļ������� | NFS (�����ļ�ϵͳ) | [UDP](#udp) |
| IP �绰 | ר��Э�� | [UDP](#udp) |
| ��ʽ��ý��ͨ�� | ר��Э�� | [UDP](#udp) |
| �ಥ | IGMP (���������Э��) | [UDP](#udp) |
| �����ʼ� | SMTP (���ʼ�����Э��) | [TCP](#tcp) |
| Զ���ն˽��� | TELNET (Զ���ն�Э��) | [TCP](#tcp) |
| ��ά�� | HTTP (���ı�����Э��) | [TCP](#tcp) |
| �ļ����� | FTP (�ļ�����Э��) | [TCP](#tcp) |
## ftp
## sftp

## ��֪�˿ں�
| **Ӧ�ó���** | FTP | TELNET | SMTP | DNS | TFTP | HTTP | SNMP | SNMP(TRAP) | HTTPS |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **��֪�˿ں�** | 21 | 23 | 25 | 53 | 69 | 80 | 161 | 162 | 443 |

# �����(transport layer)

## ���������Э��
| Э���� | ICMP | IGMP | IP | TCP | EGP | IGP | UDP | IPv6 | ESP | OSPF |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Э���ֶ�ֵ** | 1 | 2 | 4 | 6 | 8 | 9 | 17 | 41 | 50 | 89 |

## UDP
![Alt text](./img/image.png)
### UDP�ײ�
| Decimal | 2        | 2         | 2       | 2  |
|:---:|:---:|:---:|:---:|:---:|
| **Description** | [src_port](#��֪�˿ں�) | [dest_port](#��֪�˿ں�) | pkt_len | CS |

#### α�ײ�
| **Decimal** | 4 | 4 | 1 | 1 | 2 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Description** | Src_IPaddr | Dest_IPaddr | 0 | [Protocol_type](#���������Э��) | Pkt_len |
| **Value** | | | | 17 | |

## TCP
![Alt text](./img/image-1.png)
### TCP�ײ�
| **Decimal** | 2 | 2 | 4 | 4 | 4b | 6b | 1b | 1b | 1b | 1b | 1b | 1b | 2 | 2 | 2 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Description** | [src_port](#��֪�˿ں�) | [dest_port](#��֪�˿ں�) | [Seq](#seq) | Ack Seq | Pkt_len | Res | URG | ACK | PSH | RST | SYN | FIN | WINDOWS | CS | Urgent Pointer |

#### α�ײ�
| **Decimal** | 4 | 4 | 1 | 1 | 2 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Description** | Src_IPaddr | Dest_IPaddr | 0 | [Protocol_type](#���������Э��) | Pkt_len |
| **Value** | | | | 6 | |

### Seq
TCP�����е��ֽ�����ţ�ָ���Ǳ����Ķεĵ�һ���ֽڵ����


# �����(network layer)

## ���������Э��
| Э���� | IP | Novell IPX |
| :---: | :---: | :---: |
| **Э���ֶ�ֵ** | 0x0800 | 0x8137 |

## IP
### IP�ײ�
![Alt text](./img/image-2.png)
| **Decimal** | [4b] | [4b] | 1 | 2 | 2 | [1b] | [1b] | [1b] | [13b] | 1 | 1 | 2 | 4 | 4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Description** | Version | Hdr_len | [TOS](#tos) | Pkt_len | ID | MF | DF | RES | Offset | TTL | [Protocol_type](#���������Э��) | CS(hdr) | Src_ip | Dest_ip |

#### TOS
type of service����������COS��

# ������·��(data link layer)

## MAC
#### MAC֡��ʽ
![Alt text](./img/image-3.png)
| **Decimal** | 6 | 6 | 2 | 46~1500 | 4 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Description** | Src_MAC | Dest_MAC | [Protocol_type](#���������Э��) | [Packet](#mac-packet) | CRC |

#### MAC Packet
�������ֶεĳ���С�� 46 �ֽ�ʱ, MAC �Ӳ�ͻ��������ֶεĺ������һ�������� �ڵ�����ֶ�, �Ա�֤��̫���� MAC ֡��С�� 64 �ֽڡ�

# �����