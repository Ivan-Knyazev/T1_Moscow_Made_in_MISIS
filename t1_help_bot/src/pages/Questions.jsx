const Questions = ({state, setState}) => {

    // greeting: '',
    // farevell: '',
    // disc: '',
    // link_bd: '',
    // promt: '',
    // model_ai: '',
    // file_bd: null,
    // color: 'rgba(78, 163, 178, 1)',
    // font: 'Rubik',
    // name: '',
    // avatar: null,

    const handleSubmit = (e) => {
        e.preventDefault(); 
        console.log('Отправка данных формы:', state);
        fetch('https://', {
            method: 'GET',
            body: JSON.stringify(state)
        })
        .then((res) => {
        return JSON.stringify(res)
        }
    )
    .then(res => setState({
        pos: 3, 
        greeting: '',
        farevell: '',
        disc: '',
        link_bd: '',
        promt: '',
        model_ai: '',
        file_bd: null,
        color: 'rgba(78, 163, 178, 1)',
        font: 'Rubik',
        name: '',
        avatar: null,
        res
    }))
        .catch(e => console.log(e));
    };

    return(<>
    <form onSubmit={handleSubmit}>
    <div className="wrap">
    <div className="second-flex">
        <div>
    <div className="block">
            <h2>Общие фразы</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>
                    <label> Приветствие
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    greeting: e.value,
                             })
                        )}
                        ></input></label>

                        <label> Завершение диалога
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    farevell: e.value,
                             })
                        )}
                        ></input>
                        </label>
                </div>
                <label>Описание
                    <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                disc: e.value,
                             })
                        )}
                    ></input>
                    </label>
        </div>
        </div>

        <div className="block">
            <h2>База знаний</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>
                    <label>URL-ссылка на базу знаний
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    greeting: e.value,
                             })
                        )}
                        ></input></label>

                        <label> Промпт для ассистента 
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    promt: e.value,
                             })
                        )}
                        >
                        </input>
                        </label>

                    <label>Модель нейронной сети
                    <select 
                        onChange={(e) => setState(prev => ({ ...prev, model: e.target.value }))}
                    >
                        <option value="1">Option 1</option>
                        <option value="2">Option 2</option>
                        <option value="3">Option 3</option>
                    </select>
                        </label>

                </div>
                <label>Загрузить файл базы знаний
                                <input 
                        type="file"
                        onChange={(e) => {
                            const file = e.target.files[0];
                            setState(prev => ({ ...prev, file }));
                }}
            />
                        </label>
        </div>
        </div>
        <div className="block">
            <h2>Внешний вид</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>
                    <label>Цвета
                        <input type="radio"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    color: e.value,
                             })
                        )}
                        ></input></label>

                    <label>Шрифт
                    <select 
                        onChange={(e) => setState(prev => ({ ...prev, font: e.target.value }))}
                    >
                        <option value="1">Rubik</option>
                        <option value="2">Montsserat</option>
                        <option value="3">Inter</option>
                    </select>
                        </label>

                        <label>Имя ассистента
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    name: e.value,
                             })
                        )}
                        ></input></label>

                </div>
                <label>Загрузить аватар ассистента
                                <input 
                        type="file"
                        onChange={(e) => {
                            const avatar = e.target.files[0];
                            setState(prev => ({ ...prev, avatar }));
                }}/> </label>
        </div>

        </div>

        <button> onClick={() => handleSubmit()}
            Готово
        </button>
    </div>
    </div>
    </div>

    </form>
    </>)

}

export default Questions;