#include<iostream>
#include<map>
using namespace std;


int main(){

    string s="AAABBC";
    // cin>>s;

    map<char,int>mp;
    for(int i=0;i<s.size();i++){
        mp[s[i]]++;
    }
    string result;
    for(auto ele:mp){
        result.push_back(ele.first);
        result.push_back(ele.second+'0');
    }
    cout<<"The compressed data is "<< result<<endl;
}