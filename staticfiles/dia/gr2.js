

class Graph {
    /**
     
     * @param {HTMLElement} element 
     * @param {Object} options 
    
     */
    constructor(element, options = {}) {
        this.element = element
        try {
            let children = [].slice.call(element.children)
            // Modification du DOM
        this.root = this.createDivWithClass('pane')
        this.container = this.createDivWithId('chartContaine' + element.className)
        this.root.setAttribute('tabindex', '0')

        this.root.appendChild(this.container)
        this.element.appendChild(this.root)

        this.items = children.map((child) => {
            let item = this.createDivWithClass('carousel__item')

            item.appendChild(child)
            this.container.appendChild(item)
            return item
        });
        } catch (error) {
            
        }
        

        try {
            $(function () {
                $('#chartContaine' + element.className).dxCircularGauge({
                    scale: {
                        startValue: options.startValue,
    
                        endValue: options.endValue,
                        majorTick: {
                            tickInterval: 10
                        }
                    },
                    rangeContainer: {
                        backgroundColor: '#727272',
                        ranges: [
                            { startValue: 0, endValue: 10, color: '#ea1313' },
                            { startValue: 10, endValue: 40, color: '#FFBF00' },
                            { startValue: 40, endValue: 60, color: '#8DB600' },
                            { startValue: 60, endValue: 100, color: '#005fff' },
    
                        ]
                    },
                    title: {
                        /*text: 'Temperature of the Liquid in the Boiler',
                        font: { size: 28 }*/
                    },
                    value: options.value,
                });
            }
    
            );
        } catch (error) {
            
        }
       

    }


    /**
     * 
     * @param {string} className 
     * @returns {HTMLElement}
     */
    createDivWithClass(className) {
        let div = document.createElement('div')
        div.setAttribute('class', className)
        return div
    }
    /**
     * 
     * @param {string} idName 
     * @returns {HTMLElement}
     */
    createDivWithId(className) {
        let div = document.createElement('div')
        div.setAttribute('id', className)
        return div
    }

}


class Pile {
    /**
     
     * @param {HTMLElement} element 
     * @param {Object} options 
     * @param {object} [options.data] DATA  à DEUX COLONES x,y. [
            { Non_colone: nom, val: valeur },...}
     * @param {options} [options.argumentField] COLONE x POUR y
     * @param {options} [options.format] thousands: 1, millions: 2, billions: 3, trillions: 4 ,
         currency: "C", fixedpoint: "N", exponential: "", percent: "P", decimal: "D"
     
     */
    constructor(element, options = {}) {
        this.element = element
       
        
        let children = [].slice.call(element.children)

        // Modification du DOM
        this.root = this.createDivWithClass('pane')
        this.container = this.createDivWithId('chartContaine' + element.className)
        this.root.setAttribute('tabindex', '0')

        this.root.appendChild(this.container)
        this.element.appendChild(this.root)

        this.items = children.map((child) => {
            let item = this.createDivWithClass('carousel__item')

            item.appendChild(child)
            this.container.appendChild(item)
            return item
        });
        $(function () {
            if (options.data){
                var dataSource = options.data;}
            else{
                var dataSource = options.d()
            }
            var Titre = options.Titre;
            
            $('#chartContaine' + element.className).dxPieChart({
                dataSource: dataSource,
                title: Titre,
                
                
                tooltip: {
                    
                    enabled: true,
                    format: options.format,
                    percentPrecision: 2,
                    customizeText: function () {
                        return this.valueText + " - " + this.percentText;
                    }
                },
                legend: {
                    horizontalAlignment: "center",
                    verticalAlignment: "button",
                    margin: 20,
                    
                   
                },
                series: [{
                    
                    type: "doughnut",
                    argumentField: options.argumentField,
                    label: {
                        
                        visible: true,
                        format: options.format,
                        connector: {
                            visible: true
                        }
                    }
                }]
            });
        }

        );

    }


    /**
     * 
     * @param {string} className 
     * @returns {HTMLElement}
     */
    createDivWithClass(className) {
        let div = document.createElement('div')
        div.setAttribute('class', className)
        return div
    }
    /**
     * 
     * @param {string} idName 
     * @returns {HTMLElement}
     */
    createDivWithId(className) {
        let div = document.createElement('div')
        div.setAttribute('id', className)
        return div
    }

}




var k =  document.querySelector("#g2");
var taona_karazany_k =  document.querySelector("#g3");
document.addEventListener('DOMContentLoaded', function () {
    /*new Graph(document.querySelector("#g1"), {

        value: 33
    },)*/
    
    
     
    

    new Pile(document.querySelector("#g2"),{
        /**
       * @param {string} Titre
       *  @param {Array} data or @param {Array} d
       */
       data :k(),
       Titre:"Tobana anireo Katekomen",
       
        argumentField: "Mpino",
        format:"P"  /* thousands: 1, millions: 2, billions: 3, trillions: 4 ,
         currency: "C", fixedpoint: "N", exponential: "", percent: "P", decimal: "D" */
    } ,)
    new Pile(document.querySelector("#g3"),{
        /**
       * @param {string} Titre
       *  @param {Array} data or @param {Array} d
       */
       data :taona_karazany_k(),
       Titre:"Tobana anireo Ambarantogan-taona",
       
        argumentField: "Mpino",
        format:"P"  /* thousands: 1, millions: 2, billions: 3, trillions: 4 ,
         currency: "C", fixedpoint: "N", exponential: "", percent: "P", decimal: "D" */
    } ,)
})
