/* @odoo-module */


import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class ListViewAction extends Component {
    static template = "real_estate.ListView";



    setUp(){
        
    }
}

registry.category("actions").add("real_estate.action_list_view",ListViewAction);