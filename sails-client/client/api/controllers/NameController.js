/**
 * NameController
 *
 * @module		:: Controller
 * @description	:: Contains logic for handling requests.
 */

module.exports = {
	list: function(req, res) {
		
		Name.find({
			},
			function(err, data) {
			console.log(data);
		
			res.view({
				names: data
			});
		});
		
	},
	
	adamcreate: function(req, res) {
		console.log(req);
		
		Name.create({	
			label: req.param('label')
		}).done(function(err, name) {
			res.json(name);
			
		});
	}
};
