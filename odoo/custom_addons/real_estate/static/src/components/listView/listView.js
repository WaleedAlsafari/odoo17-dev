/* @odoo-module */


import { Component, useState, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class ListViewAction extends Component {
    static template = "real_estate.ListView";



    setup(){
        this.state = useState({
            'records' : []
        });
        this.orm = useService("orm");
        this.rpc= useService('rpc');
        this.loadRecords();
        // rander/refresh the component automattically each 3ms
        this.intervalId = setInterval(() => {this.loadRecords(),3000})
        onWillUnmount(() => {this.intervalId})

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
    
}

registry.category("actions").add("real_estate.action_list_view",ListViewAction);

