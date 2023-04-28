    const initOptions = {
        responseMode: 'fragment',
        flow: 'standard',
        onLoad: 'login-required'
    };
    
    function redirect() {
        console.log("Redirecting")
        window.location.href = homepage + "/Restricted-Content.html";
    }

    function initKeycloak() {
        const keycloak = new Keycloak(homepage + '/_static/keycloak_web_js.json');
        keycloak.init(initOptions).then(function(authenticated) {                
    		console.log('Init Success (' + (authenticated ? 'Authenticated token : '+JSON.stringify(keycloak) : 'Not Authenticated') + ')');
    	
    		var realm_roles = keycloak.tokenParsed.realm_access.roles;
        	console.log(authenticated ? 'Realm Roles : '+JSON.stringify(realm_roles) : 'Not Authenticated');
        	realm_roles = realm_roles.reduce((index,value) => (index[value] = true, index), {});
        
			//check if permissions exist

            if (!(realm_roles.admin === true || realm_roles.supervisor === true  ||  realm_roles.reader === true )) {
                redirect();
            } else {
                document.getElementById("hideDiv").style.display="block";
            }

                
            }).catch(function() {
                console.log('failed to initialize');
                redirect();
            });
    }