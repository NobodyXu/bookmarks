 - Here's a sample systemd unit for a network proxy stored in `/home/<user>`:
   
   ```
   [Unit]
    
   [Service]
   ExecStart=/home/<user>/exe args...

   Restart=on-failure

   User=<user>
   PrivateUsers=true

   NoNewPrivileges=true
   
   ProtectSystem=strict
   ProtectHome=read-only
   PrivateTmp=true
   ProtectProc=noaccess
   PrivateDevices=true
   ProtectHostname=true
   ProtectClock=true
   ProtectKernelTunables=true
   ProtectKernelModules=true
   ProtectKernelLogs=true
   ProtectControlGroups=true

   RemoveIPC=true
   
   [Install]
   WantedBy=multi-user.target
   ```

   If the exe and config is not stored in home, then `User=<user>` can be replaced with 
   `DynamicUser=true` and `ProtectHome` can be set to `true`.

   You can also uses:

   ```
   CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
   AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
   ```

   so that the services can bind to privileged ports.
 - systemd template unit. (Learnt from: https://fedoramagazine.org/systemd-template-unit-files/ and systemd.unit man page)
   
   Create a `name@.service` where `name` is any name you want.

   In the service, you can use `%i` to refer to the argument passed to the template.

   To actually enable an instance of this template, use `sudo systemctl enable name@param`, where `param` will be passed to `%i`.
 - Remember to add:
   
   ```
   After=network-online.target
   Wants=network-online.target
   ```

   to `[Unit]` if your service depends on network
 - How to make any port-listening service start-on-demon and auto exit when inactive using
   systemd's socket activation and `/lib/systemd/systemd-socket-proxyd`:
   
   First, we need a `listener.socket`:
   ```
    [Socket]
    # Can also be ListenDatagram or ListenSequentialPacket
    ListenStream=port
    
    [Install]
    WantedBy=sockets.target
   ```

   `listener.socket` would not be useful without `listener.service`:

   ```
   [Unit]
   BindsTo=proxy.service
   After=proxy.service
   
   Requires=listener.socket
   After=listener.socket
   
   [Service]
   # --exit-idle-time would make systemd-socket-proxyd automatically quit when
   # there is no active connection from port for more than 6m.
   #
   # To make the proxy.service quit automatically, adds 'StopWhenUnneeded=true' to its '[Unit]'.
   ExecStart=/lib/systemd/systemd-socket-proxyd --exit-idle-time='6m' 127.0.0.1:port2
   
   Restart=on-failure

   # If unix socket is used instead of 127.0.0.1, then PrivateNetwork can be enabled.
   #PrivateNetwork=yes
   
   DynamicUser=true
   PrivateUsers=true
   
   NoNewPrivileges=true
   
   ProtectSystem=strict
   ProtectHome=true
   PrivateTmp=true
   ProtectProc=noaccess
   PrivateDevices=true
   ProtectHostname=true
   ProtectClock=true
   ProtectKernelTunables=true
   ProtectKernelModules=true
   ProtectKernelLogs=true
   ProtectControlGroups=true
   
   RemoveIPC=true
   
   [Install]
   WantedBy=multi-user.target
   ```

   Then you would need to add `StopWhenUnneeded=true` to your `proxy.service`'s `[Unit]` section.

   Learnt from:
    - [systemd-socket-proxyd - freedesktop man page](https://www.freedesktop.org/software/systemd/man/systemd-socket-proxyd.html)
    - [On-demand SSH Socks proxy through systemd user units with socket-activation doesn't restart as wished](https://unix.stackexchange.com/questions/383678/on-demand-ssh-socks-proxy-through-systemd-user-units-with-socket-activation-does)
 - `systemd-analyze security $unit` to analyze security
