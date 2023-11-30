
interface GraficoProps {
    flagShow: boolean
}

function Grafico ({flagShow} : GraficoProps) {
    return (
        <div className="container">
            {flagShow && 
            <div className="grafico-teste">
                <div className="opcao">Velocidade</div>
                <div className="opcao">Aceleracao</div >
                <div className="opcao">Outros</div >
            </div>
            }
        </div>
    )
}

export default Grafico;