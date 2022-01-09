const { check } = require('express-validator/check');

class Livro {
    static validacoes() {
        return [ 
            check('titulo').isLength( { min: 15 }).withMessage('O título precisa ter, no mínimo, 15 caracteres.'),
            check('preco').isCurrency().withMessage('O preço precisa ser um valor numérico válido.')
        ];
    }
}

module.exports = Livro;