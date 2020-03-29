### How to run rootless

As `tshark` utilizes `/usr/bin/dumpcap`, we need to make sure it is runnable.

A bit of investigation of it shows that:

```
$ getcap /usr/bin/dumpcap 
/usr/bin/dumpcap = cap_net_admin,cap_net_raw+eip
$ ls -lsh /usr/bin/dumpcap
112K -rwxr-xr-- 1 root wireshark 111K Sep 27  2019 /usr/bin/dumpcap
```

So in order to run rootless, you just need to run as group `wireshark`:

```
sudo -g wireshark tshark
```
