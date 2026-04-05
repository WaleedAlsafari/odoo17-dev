/* @odoo-module */


import {Component, useState} from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";




export class FormView extends Component {
    static template = "real_estate.FormView";



    setup(){
        this.state = useState({
            name : '',
            postcode : '',
            selling_price : '',
            date_availability : ''
        });
        this.rpc = useService('rpc');
    }

    async createRecord(){
        await this.rpc('/web/dataset/call_kw', {
            model : 'estate.property',
            method : 'create',
            args : [{
                name : this.state.name,
                postcode : this.state.postcode,
                selling_price : this.state.selling_price,
                date_availability : this.state.date_availability
            }],
            kwargs : {}
        })
    }


    cancel(){
        this.state.name = '';
        this.state.postcode = '';
        this.state.selling_price = '';
        this.state.date_availability = '';
    }
    
}
