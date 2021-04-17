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
 - [systemd template unit](https://fedoramagazine.org/systemd-template-unit-files/)
