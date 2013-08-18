/**
 * UserController
 *
 * @module		:: Controller
 * @description	:: Contains logic for handling requests.
 */

module.exports = {
	list: function(req, res) {
		
		User.find({
			},
			function(err, data) {
			console.log(data);
		
			res.view({
				users: data
			});
		});
		
	},
	
	create: function(req, res) {
		User.create({
			name: 'Adam',
			email: 'adam@adam.com',
			password: 'test'
		}).done(function(err, user) {
			
		});
	}
};
