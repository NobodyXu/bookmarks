 1. Add the following file to `/usr/local/bin/start_jenkins.sh`:
    
    ```bash
    #!/bin/bash
    # /etc/init.d/jenkins
    # debian-compatible jenkins startup script.
    # Amelia A Lewis <alewis@ibco.com>
    #
    
    DESC="Jenkins Automation Server"
    NAME=jenkins
    
    [ -r /etc/default/$NAME ] && . /etc/default/$NAME
    
    JAVA=`type -p java`
    
    if [ "$JENKINS_ENABLE_ACCESS_LOG" = "yes" ]; then
        JENKINS_ARGS="$JENKINS_ARGS --accessLoggerClassName=winstone.accesslog.SimpleAccessLogger --simpleAccessLogger.format=combined --simpleAccessLogger.file=/var/log/$NAME/access_log"
    fi
    
    # Exit if not supposed to run standalone
    if [ "$RUN_STANDALONE" = "false" ]; then
        echo "Not configured to run standalone" >&2
        exit 1
    fi
    
    # Make sure there exists a java executable, it may not be allways the case
    if [ -z "$JAVA" ]; then
        echo "ERROR: No Java executable found in current PATH: $PATH" >&2
        echo "If you actually have java installed on the system make sure the executable is in the aforementioned path and that 'type -p java' returns the java executable path" >&2
        exit 1
    fi
    
    # Which Java versions can be used to run Jenkins
    JAVA_ALLOWED_VERSIONS=( "18" "110" )
    # Work out the JAVA version we are working with:
    JAVA_VERSION=$($JAVA -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*".*/\1\2/p;')
    
    if [[ ${JAVA_ALLOWED_VERSIONS[*]} =~ "$JAVA_VERSION" ]]; then
        echo "Correct java version found" >&2
    else
        echo "Found an incorrect Java version" >&2
        echo "Java version found:" >&2
        echo $($JAVA -version) >&2
        echo "Aborting" >&2
        exit 1
    fi
    
    # load environments
    if [ -r /etc/default/locale ]; then
      . /etc/default/locale
      export LANG LANGUAGE
    elif [ -r /etc/environment ]; then
      . /etc/environment
      export LANG LANGUAGE
    fi
    
    # Load the VERBOSE setting and other rcS variables
    . /lib/init/vars.sh
    
    # Define LSB log_* functions.
    # Depend on lsb-base (>= 3.0-6) to ensure that this file is present.
    . /lib/lsb/init-functions
    
    check_tcp_port() {
        local service=$1
        local assigned=$2
        local default=$3
        local assigned_address=$4
        local default_address=$5
    
        if [ -n "$assigned" ]; then
            port=$assigned
        else
            port=$default
        fi
    
        if [ -n "$assigned_address" ]; then
            address=$assigned_address
        else
            address=$default_address
        fi
    
        count=`netstat --listen --numeric-ports | grep $address\:$port[[:space:]] | grep -c . `
    
        if [ $count -ne 0 ]; then
            echo "The selected $service port ($port) on address $address seems to be in use by another program "
            echo "Please select another address/port combination to use for $NAME"
            return 1
        fi
    }
    
    # Verify that the jenkins port is not already in use, winstone does not exit
    # even for BindException
    check_tcp_port "http" "$HTTP_PORT" "8080" "$HTTP_HOST" "0.0.0.0" || exit 1
    
    # the default location is /var/run/jenkins/jenkins.pid but the parent directory needs to be created
    mkdir `dirname $PIDFILE` > /dev/null 2>&1 || true
    chown $JENKINS_USER `dirname $PIDFILE`
    echo "$BASHPID" >$PIDFILE
    
    export JENKINS_HOME=$JENKINS_HOME
    exec $JAVA $JAVA_ARGS -jar $JENKINS_WAR $JENKINS_ARGS
    ```

 2. `sudo systemctl stop jenkins.service` to stop the default service in `/etc/init.d/jenkins`.
 3. Add the following to `/etc/systemd/system/jenkins.service`:
 
    ```systemd
    [Unit]
    Description=Jenkins Automation Server
    After=network.target
    Requires=network.target
    
    [Service]
    Type=simple
    
    PIDFile=/var/run/jenkins/jenkins.pid
    ExecStart=/usr/local/bin/start_jenkins.sh
    
    Restart=on-failure
    RestartSec=20
    
    User=jenkins
    Group=jenkins
    NoNewPrivileges=yes
    SecureBits=noroot
    
    ProtectSystem=full
    ProtectHome=yes
    PrivateTmp=true
    PrivateDevices=true
    ProtectKernelTunables=true
    ProtectControlGroups=true
    
    [Install]
    WantedBy=multi-user.target
    ```
    
    Advantage of systemd over the default `/etc/init.d/jenkins` is that
     - no systemd user unit will be started for `jenkins` due to use of `su -l`
     - no need for an extra idle process `daemon`
     - `jenkins` is sandboxed: no new privilege (no `sudo`) and cannot modify `/usr`, `/boot`, `/etc` and cannot access `/home`, `/root`,
       devices other than `/dev/zero`, `/dev/null`, `/dev/random`, access of kernel tunable and control groups are denied.
     - `jenkins` will not share `/tmp/` with any other process. Instead, its `/tmp` will only be visible to itself and it cannot access global `/tmp`.
    
 4. Then `sudo systemctl enable jenkins.service` and `sudo systemctl start jenkins.service`.
    Make sure it is started and running.
