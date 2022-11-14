    const initOptions = {
        responseMode: 'fragment',
        flow: 'standard',
        onLoad: 'login-required'
    };
    
    function redirect() {
        window.location.href = homepage + "/Restricted-Content.html";
    }

    function initKeycloak() {
        const keycloak = new Keycloak(homepage + '/_static/keycloak_web_js.json');
        keycloak.init(initOptions).then(function(authenticated) {                
    		console.log('Init Success (' + (authenticated ? 'Authenticated token : '+JSON.stringify(keycloak) : 'Not Authenticated') + ')');
    	
    		var realm_roles = keycloak.tokenParsed.realm_access.roles;
        	console.log(authenticated ? 'Realm Roles : '+JSON.stringify(realm_roles) : 'Not Authenticated');
        	realm_roles = realm_roles.reduce((index,value) => (index[value] = true, index), {});
        
        	var resource_access = keycloak.tokenParsed.resource_access;
        	console.log(authenticated ? 'Resource Access : '+JSON.stringify(resource_access) : 'Not Authenticated');

        	var groups = keycloak.tokenParsed.groups;
        	console.log(authenticated ? 'Groups : '+JSON.stringify(groups) : 'Not Authenticated');
        	groups = groups.reduce((index,value) => (index[value] = true, index), {});


			//check if key exists
			const hasKey = resource_access.hasOwnProperty('web_js');

			if(hasKey) {
        		var resource_roles = keycloak.tokenParsed.resource_access.web_js.roles;

        		console.log(authenticated ? 'Resource Roles : '+JSON.stringify(resource_roles) : 'Not Authenticated');
        		resource_roles = resource_roles.reduce((index,value) => (index[value] = true, index), {});
                
        		if (!((realm_roles.admin === true || realm_roles.supervisor === true  ||  resource_roles.access_admin_docs === true ))) 
        			redirect();

            } else {

      
                if (!(realm_roles.admin === true || realm_roles.supervisor === true )) 
                	redirect();
            	
            }
                
            }).catch(function() {
                console.log('failed to initialize');
            });
    }