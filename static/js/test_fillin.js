const ids = [
    "id_ssn",
    "id_cc_num",
    "id_first",
    "id_last",
    "id_gender",
    "id_street",
    "id_city",
    "id_state",
    "id_zip",
    "id_lat",
    "id_long",
    "id_city_pop",
    "id_job",
    "id_dob",
    "id_acct_num",
    "id_trans_num",
    "id_trans_date",
    "id_trans_time",
    "id_unix_time",
    "id_category",
    "id_amt",
    "id_merchant",
    "id_merch_lat",
    "id_merch_long"
];

const fraudulent = {
    "id_ssn": "8095-6382161-6",
    "id_cc_num": "4770417457749054840",
    "id_first": "Jeffrey",
    "id_last": "Hall",
    "id_gender": "M",
    "id_street": "B14 L73 Kelley Subdivision 3, Maxwell Avenue",
    "id_city": "Balanga",
    "id_state": "PH",
    "id_zip": "96061",
    "id_lat": "14.6833",
    "id_long": "120.5333",
    "id_city_pop": "96061",
    "id_job": "Public relations account executive",
    "id_dob": "1951-06-28",
    "id_acct_num": "485205535176",
    "id_trans_num": "8a6539ced1e2ec85bf4a1ed11437a80f",
    "id_trans_date": "2021-11-23",
    "id_trans_time": "23:07:03",
    "id_unix_time": "1637708823",
    "id_category": "entertainment",
    "id_amt": "401.42",
    "id_merchant": "Starmedia Entertainment",
    "id_merch_lat": "15.116130",
    "id_merch_long": "120.455907"
}

const non_fraudulent = {
    "id_ssn": "1598-9383551-0",
    "id_cc_num": "502018431499",
    "id_first": "Jacob",
    "id_last": "Ryan",
    "id_gender": "M",
    "id_street": "3F Citrine Suites Tower 4, 6306 Comet Road",
    "id_city": "San Fernando",
    "id_state": "PH",
    "id_zip": "306659",
    "id_lat": "15.0333",
    "id_long": "120.6833",
    "id_city_pop": "306659",
    "id_job": "Programmer, multimedia",
    "id_dob": "1956-10-19",
    "id_acct_num": "526103346254",
    "id_trans_num": "093c27379a03b19a115fd1a4e338974b",
    "id_trans_date": "2020-01-18",
    "id_trans_time": "18:37:08",
    "id_unix_time": "1579372628",
    "id_category": "food_dining",
    "id_amt": "57.16",
    "id_merchant": "The Moment Group",
    "id_merch_lat": "14.457212",
    "id_merch_long": "121.247686"
}

function fraudfillin(){
    for (const input_id of ids){
        document.getElementById(input_id).value = fraudulent[input_id];
    }
}

function nonfraudfillin(){
    for (const input_id of ids){
        document.getElementById(input_id).value = non_fraudulent[input_id];
    }
}