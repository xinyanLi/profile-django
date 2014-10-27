var app = angular.module("profileApp", []);
app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller("profileController", function($scope, $http, $log) {

	$scope.curPerson = {
		first_name: '',
		last_name:'',
		email: '',
		phone: ''
	};

	$scope.initialize = function(message) {
		$scope.load();
	};
	
	$scope.load = function() {
		$http.get('/api/profiles/').then(function(response){       // promise service
			$scope.people =  response.data;
			console.log('load then', response.data);
		});
	};


	$scope.save = function() {
		$http.post('/api/profiles/', $scope.curPerson).then(function(response){      
			$scope.load();
			$scope.curPerson = {};
			console.log('save then', response);
		});
	};

	$scope.delete = function(person) {
		console.log('person', person);
		$http.delete('/api/profiles/'+person.id).then(function(response){      
			$scope.load();
			console.log('delete then', response);
		});
			$scope.load();

	};	
});