# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the ios_snmp_server module
"""


class Snmp_serverArgs(object):  # pylint: disable=R0903
    """The arg spec for the ios_snmp_server module"""

    argument_spec = {
        "config": {
            "options": {
                "accounting": {"options": {"command": {"type": "str"}}, "type": "dict"},
                "cache": {"type": "int"},
                "chassis_id": {"type": "str"},
                "communities": {
                    "elements": "dict",
                    "options": {
                        "acl_v4": {"type": "str"},
                        "acl_v6": {"type": "str"},
                        "name": {"type": "str"},
                        "ro": {"type": "bool"},
                        "rw": {"type": "bool"},
                        "view": {"type": "str"},
                    },
                    "type": "list",
                },
                "contact": {"type": "str"},
                "context": {"elements": "str", "type": "list"},
                "drop": {
                    "options": {"unknown_user": {"type": "bool"}, "vrf_traffic": {"type": "bool"}},
                    "type": "dict",
                },
                "engine_id": {
                    "elements": "dict",
                    "options": {
                        "id": {"type": "str"},
                        "local": {"type": "bool"},
                        "remote": {
                            "options": {
                                "host": {"type": "str"},
                                "udp_port": {"type": "int"},
                                "vrf": {"type": "str"},
                            },
                            "type": "dict",
                        },
                    },
                    "type": "list",
                },
                "file_transfer": {
                    "options": {
                        "access_group": {"type": "str"},
                        "protocol": {"type": "list", "elements": "str"},
                    },
                    "type": "dict",
                },
                "groups": {
                    "elements": "dict",
                    "options": {
                        "context": {"type": "str"},
                        "version_option": {"choices": ["auth", "noauth", "priv"], "type": "str"},
                        "group": {"type": "str"},
                        "notify": {"type": "str"},
                        "read": {"type": "str"},
                        "version": {"choices": ["v1", "v3", "v2c"], "type": "str"},
                        "write": {"type": "str"},
                        "acl_v4": {"type": "str"},
                        "acl_v6": {"type": "str"},
                    },
                    "type": "list",
                },
                "hosts": {
                    "elements": "dict",
                    "options": {
                        "host": {"type": "str"},
                        "informs": {"type": "bool"},
                        "community_string": {"type": "str"},
                        "traps": {"type": "list", "elements": "str"},
                        "version": {"choices": ["1", "2c", "3"], "type": "str"},
                        "version_option": {"choices": ["auth", "noauth", "priv"], "type": "str"},
                        "vrf": {"type": "str"},
                    },
                    "type": "list",
                },
                "if_index": {"type": "bool"},
                "inform": {
                    "options": {
                        "pending": {"type": "int"},
                        "retries": {"type": "int"},
                        "timeout": {"type": "int"},
                    },
                    "type": "dict",
                },
                "ip": {
                    "options": {"dscp": {"type": "int"}, "precedence": {"type": "int"}},
                    "type": "dict",
                },
                "location": {"type": "str"},
                "manager": {"type": "int"},
                "packet_size": {"type": "int"},
                "password_policy": {
                    "elements": "dict",
                    "no_log": False,
                    "options": {
                        "change": {"type": "int"},
                        "digits": {"type": "int"},
                        "lower_case": {"type": "int"},
                        "max_len": {"type": "int"},
                        "min_len": {"type": "int"},
                        "policy_name": {"type": "str"},
                        "special_char": {"type": "int"},
                        "upper_case": {"type": "int"},
                        "username": {"type": "str"},
                    },
                    "type": "list",
                },
                "queue_length": {"type": "int"},
                "source_interface": {"type": "str"},
                "system_shutdown": {"type": "bool"},
                "trap_source": {"type": "str"},
                "trap_timeout": {"type": "int"},
                "traps": {
                    "options": {
                        "auth_framework": {
                            "options": {
                                "sec_violation": {"type": "bool"},
                                "enable": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "bfd": {
                            "options": {
                                "enable": {"type": "bool"},
                                "session_down": {"type": "bool"},
                                "session_up": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "bgp": {
                            "options": {
                                "cbgp2": {"type": "bool"},
                                "enable": {"type": "bool"},
                                "state_changes": {
                                    "options": {
                                        "all": {"type": "bool"},
                                        "backward_trans": {"type": "bool"},
                                        "limited": {"type": "bool"},
                                        "enable": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "threshold": {
                                    "options": {"prefix": {"type": "bool"}},
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "bridge": {
                            "options": {
                                "newroot": {"type": "bool"},
                                "enable": {"type": "bool"},
                                "topologychange": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "casa": {"type": "bool"},
                        "cef": {
                            "options": {
                                "inconsistency": {"type": "bool"},
                                "peer_fib_state_change": {"type": "bool"},
                                "peer_state_change": {"type": "bool"},
                                "resource_failure": {"type": "bool"},
                                "enable": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "cnpd": {"type": "bool"},
                        "config": {"type": "bool"},
                        "config_copy": {"type": "bool"},
                        "config_ctid": {"type": "bool"},
                        "cpu": {
                            "options": {"enable": {"type": "bool"}, "threshold": {"type": "bool"}},
                            "type": "dict",
                        },
                        "dhcp": {"type": "bool"},
                        "dlsw": {
                            "options": {
                                "circuit": {"type": "bool"},
                                "enable": {"type": "bool"},
                                "tconn": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "eigrp": {"type": "bool"},
                        "entity": {"type": "bool"},
                        "energywise": {"type": "bool"},
                        "envmon": {
                            "options": {
                                "fan": {
                                    "options": {
                                        "shutdown": {"type": "bool"},
                                        "enable": {"type": "bool"},
                                        "status": {"type": "bool"},
                                        "supply": {"type": "bool"},
                                        "temperature": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "shutdown": {"type": "bool"},
                                "status": {"type": "bool"},
                                "supply": {"type": "bool"},
                                "temperature": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "ethernet": {
                            "options": {
                                "cfm": {
                                    "options": {
                                        "alarm": {"type": "bool"},
                                        "cc": {
                                            "type": "dict",
                                            "options": {
                                                "config": {"type": "bool"},
                                                "cross_connect": {"type": "bool"},
                                                "loop": {"type": "bool"},
                                                "mep_down": {"type": "bool"},
                                                "mep_up": {"type": "bool"},
                                            },
                                        },
                                        "crosscheck": {
                                            "type": "dict",
                                            "options": {
                                                "mep_missing": {"type": "bool"},
                                                "mep_unknown": {"type": "bool"},
                                                "service_up": {"type": "bool"},
                                            },
                                        },
                                    },
                                    "type": "dict",
                                },
                                "evc": {
                                    "options": {
                                        "create": {"type": "bool"},
                                        "delete": {"type": "bool"},
                                        "status": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "event_manager": {"type": "bool"},
                        "flowmon": {"type": "bool"},
                        "firewall": {
                            "options": {
                                "enable": {"type": "bool"},
                                "serverstatus": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "frame_relay": {
                            "options": {
                                "enable": {"type": "bool"},
                                "subif": {
                                    "options": {
                                        "count": {"type": "int"},
                                        "interval": {"type": "int"},
                                        "enable": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "fru_ctrl": {"type": "bool"},
                        "hsrp": {"type": "bool"},
                        "ike": {
                            "options": {
                                "policy": {
                                    "options": {
                                        "add": {"type": "bool"},
                                        "delete": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "tunnel": {
                                    "options": {
                                        "start": {"type": "bool"},
                                        "stop": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "ipmulticast": {"type": "bool"},
                        "ipsec": {
                            "options": {
                                "cryptomap": {
                                    "options": {
                                        "add": {"type": "bool"},
                                        "attach": {"type": "bool"},
                                        "delete": {"type": "bool"},
                                        "detach": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "too_many_sas": {"type": "bool"},
                                "tunnel": {
                                    "options": {
                                        "start": {"type": "bool"},
                                        "stop": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "ipsla": {"type": "bool"},
                        "l2tun": {
                            "options": {
                                "pseudowire_status": {"type": "bool"},
                                "session": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "msdp": {"type": "bool"},
                        "mvpn": {"type": "bool"},
                        "mpls_vpn": {"type": "bool"},
                        "ospf": {
                            "options": {
                                "cisco_specific": {
                                    "options": {
                                        "error": {"type": "bool"},
                                        "lsa": {"type": "bool"},
                                        "retransmit": {"type": "bool"},
                                        "state_change": {
                                            "options": {
                                                "nssa_trans_change": {"type": "bool"},
                                                "shamlink": {
                                                    "options": {
                                                        "interface": {"type": "bool"},
                                                        "neighbor": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "error": {"type": "bool"},
                                "retransmit": {"type": "bool"},
                                "lsa": {"type": "bool"},
                                "state_change": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "pim": {
                            "options": {
                                "invalid_pim_message": {"type": "bool"},
                                "neighbor_change": {"type": "bool"},
                                "rp_mapping_change": {"type": "bool"},
                                "enable": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "vrfmib": {
                            "options": {
                                "vrf_up": {"type": "bool"},
                                "vrf_down": {"type": "bool"},
                                "vnet_trunk_up": {"type": "bool"},
                                "vnet_trunk_down": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "pki": {"type": "bool"},
                        "rsvp": {"type": "bool"},
                        "isis": {"type": "bool"},
                        "pw_vc": {"type": "bool"},
                        "snmp": {
                            "options": {
                                "authentication": {"type": "bool"},
                                "coldstart": {"type": "bool"},
                                "linkdown": {"type": "bool"},
                                "linkup": {"type": "bool"},
                                "warmstart": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "syslog": {"type": "bool"},
                        "transceiver_all": {"type": "bool"},
                        "tty": {"type": "bool"},
                        "vrrp": {"type": "bool"},
                    },
                    "type": "dict",
                },
                "users": {
                    "elements": "dict",
                    "options": {
                        "acl_v6": {"type": "str"},
                        "acl_v4": {"type": "str"},
                        "authentication": {
                            "no_log": False,
                            "type": "dict",
                            "options": {
                                "algorithm": {"type": "str", "choices": ["md5", "sha"]},
                                "password": {"type": "str", "no_log": True},
                            },
                        },
                        "encryption": {
                            "no_log": False,
                            "type": "dict",
                            "options": {
                                "priv": {"type": "str", "choices": ["3des", "aes", "des"]},
                                "priv_option": {"type": "str"},
                                "password": {"type": "str", "no_log": True},
                            },
                        },
                        "group": {"type": "str"},
                        "remote": {"type": "str"},
                        "udp_port": {"type": "int"},
                        "username": {"type": "str"},
                        "version": {"choices": ["v1", "v2c", "v3"], "type": "str"},
                        "version_option": {"choices": ["encrypted"], "type": "str"},
                        "vrf": {"type": "str"},
                    },
                    "type": "list",
                },
                "views": {
                    "elements": "dict",
                    "options": {
                        "excluded": {"type": "bool"},
                        "family_name": {"type": "str"},
                        "included": {"type": "bool"},
                        "name": {"type": "str"},
                    },
                    "type": "list",
                },
            },
            "type": "dict",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
