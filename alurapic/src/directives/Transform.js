export default {

    bind(el, binding, vnode) {

        let current = 0;
        el.addEventListener('dblclick', function() {
            let incremento = binding.value || 90; // esta declaração é um teste: incremento recebe o valor da diretiva OU 90
            let efeito;

            if (!binding.arg || binding.arg == 'rotate') {
                if (binding.value.incremento) incremento = binding.value.incremento;

                if (binding.modifiers.reverse) {
                    current -= incremento;
                } else {
                    current += incremento;
                }
                efeito = `rotate(${current}deg)`;
            } else if (binding.arg == 'scale') {
                efeito = `scale(${incremento})`;
            }
            if (binding.modifiers.animar) el.style.transition = "transform 0.5s";;
            el.style.transform = efeito;
        });
    }

};
