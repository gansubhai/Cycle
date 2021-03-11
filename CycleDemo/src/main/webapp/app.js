//Create angular controller.
var app = angular.module('googleAapApp', []);
app.controller('googleAapCtrl', function($scope, $http) {
	console.log("googleAapCtrl initialized ...")
	$scope.highlighters = [];
	$scope.gMap = null;
	$scope.selectedCity = "None";
	$scope.showLoaderImage=false;
	var winInfo = new google.maps.InfoWindow();
	var googleMapOption = {
		zoom : 6,
		center : new google.maps.LatLng(40, -73),
		mapTypeId : google.maps.MapTypeId.TERRAIN
	};

	$scope.gMap = new google.maps.Map(document.getElementById('googleMap'),
			googleMapOption);

	/*
	 * var createHighlighter = function(citi) {
	 * 
	 * var citiesInfo = new google.maps.Marker({ map: $scope.gMap, position: new
	 * google.maps.LatLng(citi.lat, citi.long), title: citi.city });
	 * 
	 * citiesInfo.content = '<div>' + citi.desc + '</div>';
	 * 
	 * google.maps.event.addListener(citiesInfo, 'click', function() {
	 * winInfo.setContent('<h1>' + citiesInfo.title + '</h1>' +
	 * citiesInfo.content); winInfo.open($scope.gMap, citiesInfo); });
	 * $scope.highlighters.push(citiesInfo); };
	 */
	
	var createHighlighterCustom = function(citi) {
		$scope.gMap = null;
		$scope.highlighters = [];
		var winInfo = new google.maps.InfoWindow();

		var googleMapOption = {
			zoom : 6,
			center : new google.maps.LatLng(40, -73),
			mapTypeId : google.maps.MapTypeId.TERRAIN
		};

		$scope.gMap = new google.maps.Map(document.getElementById('googleMap'),
				googleMapOption);

		var citiesInfo = new google.maps.Marker({
			map : $scope.gMap,
			position : new google.maps.LatLng(citi.lat, citi.longi)
			/*icon : "http://maps.google.com/mapfiles/ms/icons/green-dot.png"*/

		});

		$scope.highlighters.push(citiesInfo);
	};

	//
	$scope.initLoad = function() {
		$scope.showLoaderImage=true;
		$http.get("/getCities").then(function sucessCallback(response) {
			console.log("response from  webservice getCities")
			console.log(response.data)
			$scope.names = response.data;
			$scope.names.push("Choose here");
			$scope.selectedCity ="Choose here";
			$scope.showLoaderImage=false;
		},

		function errorCallback(response) {
			console.log("Error in getCities")
			$scope.showLoaderImage=false;
		});
	}

	$scope.search = function() {
		$scope.showLoaderImage=true;
		console.log("Looking for " + $scope.selectedCity)
		if($scope.selectedCity!="Choose here")
			{
			var data = {
					'inputCity' : $scope.selectedCity
				};
				$http.post('/getAddress', JSON.stringify(data)).then(
						function sucessCallback(response) {
							console.log("response from  webservice getAddress")
							var output = response.data["address"];
							console.log(response.data);
							for (i = 0; i < output.length; i++) {
								createHighlighterCustom(output[i]);
							}
							$scope.showLoaderImage=false;
						}, function errorCallback(error) {
							console.log("Error in getAddress");
							$scope.showLoaderImage=false;
						});
			}
		
	}

});
// For Station
app
		.controller(
				'stationCtrl',
				function($scope, $http) {
					console.log("stationCtrl initialized ...")
					$scope.highlighters = [];
					$scope.gMap = null;
					$scope.selectedStation = "None";
					$scope.showLoaderImage=false;
					var winInfo = new google.maps.InfoWindow();
					var googleMapOption = {
						zoom : 6,
						center : new google.maps.LatLng(40, -73),
						mapTypeId : google.maps.MapTypeId.TERRAIN
					};
					$scope.gMap = new google.maps.Map(document
							.getElementById('googleStationMap'),
							googleMapOption);

					var createHighlighterCustom = function(bikeStation,
							crashAddressList) {
						$scope.gMap = null;
						$scope.highlighters = [];
						const svgMarker = {
							path : "M10.453 14.016l6.563-6.609-1.406-1.406-5.156 5.203-2.063-2.109-1.406 1.406zM12 2.016q2.906 0 4.945 2.039t2.039 4.945q0 1.453-0.727 3.328t-1.758 3.516-2.039 3.070-1.711 2.273l-0.75 0.797q-0.281-0.328-0.75-0.867t-1.688-2.156-2.133-3.141-1.664-3.445-0.75-3.375q0-2.906 2.039-4.945t4.945-2.039z",
							fillColor : "blue",
							fillOpacity : 0.6,
							strokeWeight : 0,
							rotation : 0,
							scale : 2,
							anchor : new google.maps.Point(15, 30),
						};
						var winInfo = new google.maps.InfoWindow();

						var googleMapOption = {
							zoom : 6,
							center : new google.maps.LatLng(40, -73),
							mapTypeId : google.maps.MapTypeId.TERRAIN
						};

						$scope.gMap = new google.maps.Map(document
								.getElementById('googleStationMap'),
								googleMapOption);

						var citiesInfo = new google.maps.Marker({
							map : $scope.gMap,
							position : new google.maps.LatLng(bikeStation.lat,
									bikeStation.longi),
							/*
							 * icon:
							 * "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
							 */
							icon : svgMarker,
							optimized : false

						});

						$scope.highlighters.push(citiesInfo);

						// crsah Addrss
						for (j = 0; j < crashAddressList.length; j++) {
							var crashInfo = new google.maps.Marker({
								map : $scope.gMap,
								position : new google.maps.LatLng(
										crashAddressList[j].lat,
										crashAddressList[j].longi)

							});

							$scope.highlighters.push(crashInfo);
						}
					};

					//
					$scope.initStationLoad = function() {
						$scope.showLoaderImage=true;
						$http
								.get("/getBikeStation")
								.then(
										function sucessCallback(response) {
											console
													.log("response from webservice getBikeStation")
											console.log(response.data)
											$scope.stationNames = response.data;
											$scope.stationNames.push("Choose here");
											$scope.selectedStation="Choose here";
											$scope.showLoaderImage=false;
										},

										function errorCallback(response) {
											console
													.log("Error in getBikeStation")
													$scope.showLoaderImage=false;
										});
					}

					$scope.searchCrashes = function() {
						$scope.showLoaderImage=true;
						console.log("Looking for " + $scope.selectedStation)
							if($scope.selectedStation!="Choose here")
								{
								var data = {
										'inputBikeStation' : $scope.selectedStation
									};
									$http
											.post('/getCrashNearByAddress',
													JSON.stringify(data))
											.then(
													function sucessCallback(response) {
														console
														.log("response from webservice getCrashNearByAddress")
														var output = response.data["bikeStationAddress"];
														console.log(response.data);
														for (i = 0; i < output.length; i++) {
															createHighlighterCustom(
																	output[i],
																	response.data["crashAddress"]);
														}
														$scope.showLoaderImage=false;

													}, function errorCallback(error) {
														console.log("Error in getAddress");
														$scope.showLoaderImage=false;
													});
								}
						
					}

				});
