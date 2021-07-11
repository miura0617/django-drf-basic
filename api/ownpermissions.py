from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):

    # has_object_permission関数をオーバライド
    def has_object_permission(self, request, view, obj):
        # GET/POSTの既存のDBに影響与えないものは許容し、
        # PUT/DELETEのように既存のDBに影響を与えるものは拒否するようにする
        # SAFE_METHODが新規作成や取得するだけを意味する
        # これにより、GET/POSTのみ許容するようpermissionを作れる
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
