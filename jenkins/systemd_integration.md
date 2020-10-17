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
