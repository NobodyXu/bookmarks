 - Here's a sample systemd unit for a network proxy stored in `/home/<user>`:
   
   ```
   [Unit]
    
   [Service]
   ExecStart=/home/<user>/exe args...

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
 - systemd template unit. (Learnt from: https://fedoramagazine.org/systemd-template-unit-files/ and systemd.unit man page)
   
   Create a `name@.service` where `name` is any name you want.

   In the service, you can use `%i` to refer to the argument passed to the template.

   To actually enable an instance of this template, use `sudo systemctl enable name@param`, where `param` will be passed to `%i`.
