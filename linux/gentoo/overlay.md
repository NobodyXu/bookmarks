 1. Update overlay list using `sudo layman -L`
 2. Add overlay via `sudo layman -a <overlay_name>`
 3. Update overlays using `sudo layman -S` or `sudo eix-sync` which updates all repositories (official and overlays).
 4. [How to view all packages in some overlay?](https://unix.stackexchange.com/questions/57178/how-to-view-all-packages-in-some-overlay)
    
    ```
    eix --in-overlay <OVERLAY_NAME>
    ```
