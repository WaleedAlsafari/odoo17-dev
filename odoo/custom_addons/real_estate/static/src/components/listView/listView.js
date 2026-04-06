/* @odoo-module */


import { Component, useState, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import {FormView} from "@real_estate/components/formView/formView"

export class ListViewAction extends Component {
    static template = "real_estate.ListView";
    static components = {FormView};


    setup(){
        this.state = useState({
            'records' : []
        });
        this.orm = useService("orm");
        this.rpc= useService('rpc');
        this.loadRecords();
        // rander/refresh the component automattically each 3ms
    //    this.intervalId = setInterval(() => {this.loadRecords(),3000})
    //    onWillUnmount(() => {clearInterval(this.intervalId)})

    };

    // async loadRecords(){
    //     const result = await this.orm.searchRead("estate.property", [], []);
    //     this.state.records = result;
    // };
    async loadRecords(){
        const result = await this.rpc("/web/dataset/call_kw", {
            model : 'estate.property',
            method : 'search_read',
            args : [[]],
            kwargs : {fields: ['id', 'name', 'postcode', 'selling_price', 'date_availability']}
        });
        this.state.records = result;
    };

    async createProperty(){
         await this.rpc("/web/dataset/call_kw", {
            model : 'estate.property',
            method : 'create',
            args : [{
                name : 'propertyOWL',
                postcode : '12345',
                selling_price : 9999,
                description : 'test'

            }],
            kwargs : {}
        });

        this.loadRecords()
    }

    async deleteRecord(recordId){
        await this.rpc("/web/dataset/call_kw", {
            model : 'estate.property',
            method : 'unlink',
            args : [recordId],
            kwargs : {}
        })
        this.loadRecords()
      
    }



    toggleCreateForm(){
        this.state.showFormView = !this.state.showFormView;
    
    }

  
}

registry.category("actions").add("real_estate.action_list_view",ListViewAction);

