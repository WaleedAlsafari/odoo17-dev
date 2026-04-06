/* @odoo-module */


import {Component, useState} from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";




export class FormView extends Component {
    static template = "real_estate.FormView";



    setup(){
        this.state = useState({
            name : '',
            postcode : '',
            bedrooms : '',
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
                postcode : this.state.bedrooms,
                selling_price : this.state.selling_price,
                date_availability : this.state.date_availability
            }],
            kwargs : {}
        })
        this.props.loadRecords();
        
    }


    cancel(){
        this.state.name = '';
        this.state.postcode = '';
        this.state.bedrooms = '';
        this.state.selling_price = '';
        this.state.date_availability = '';
    }
    
}
