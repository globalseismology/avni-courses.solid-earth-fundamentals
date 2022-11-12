    const keycloak = Keycloak('https://portal.globalseismology.org/files/js/keycloak_web_js.json')
    const initOptions = {
        responseMode: 'fragment',
        flow: 'standard',
        onLoad: 'login-required'
    };

    function redirect() {
        window.location.href = "https://portal.globalseismology.org/courses/solid-earth-fundamentals/fall2022/welcome.html";
    }
    keycloak.init(initOptions).success(function(authenticated) {     
        console.log('Init Success (' + (authenticated ? 'Authenticated token : '+JSON.stringify(keycloak) : 'Not Authenticated') + ')');
    	
    	var realm_roles = keycloak.tokenParsed.realm_access.roles;
        console.log(authenticated ? 'Realm Roles : '+JSON.stringify(realm_roles) : 'Not Authenticated');
        realm_roles = realm_roles.reduce((index,value) => (index[value] = true, index), {});
        
        var resource_roles = keycloak.tokenParsed.resource_access.web_js.roles;
        console.log(authenticated ? 'Resource Roles : '+JSON.stringify(resource_roles) : 'Not Authenticated');
        resource_roles = resource_roles.reduce((index,value) => (index[value] = true, index), {});
                
        if (realm_roles.admin !== true || realm_roles.supervisor !== true  || resource_roles.access_admin_docs !== true ) console
            //redirect();
            
    }).error(function() {
			console.log('Init Error')
    });