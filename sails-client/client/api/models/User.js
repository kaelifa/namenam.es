/**
 * USer
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 *
 */

var UserModel = {
	
	attributes: {
		name:		'STRING',
		email:		'STRING',
		password:	'STRING',
	
		// Override toJSON instance method
		// to remove password value
		toJSON: function() {
			var obj = this.toObject();
			delete obj.password;
			return obj;
		}
	}
};

module.exports = UserModel;